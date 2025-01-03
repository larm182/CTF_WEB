#!/usr/bin/python
#-*- coding: utf-8 -*-
#Autor: Luis Angel Ramirez Mendoza

from flask import Flask, render_template, request, redirect, url_for, session, flash
import os
import sqlite3



app = Flask(__name__)
app.secret_key = os.urandom(24)

# Conectar a la base de datos
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


def authenticate_user(username, password):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Buscar el usuario en la base de datos
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    user = cursor.fetchone()

    conn.close()

    # Si el usuario existe, devolver True, de lo contrario False
    return user is not None 

    
@app.route('/')
def index():
    return render_template('index.html')

# Reto XSS
@app.route('/xss_flag', methods=['GET', 'POST'])
def xss_flag():
    required_payload = '<script>alert("flag_1");</script>'
    if request.method == 'POST':
        user_input = request.form.get('user_input')
        if user_input == required_payload:
            return render_template('flag_1.html', user_input=user_input)
    return render_template('xss_flag.html')

# Reto SQL Injection
@app.route('/sql_injection_flag', methods=['GET', 'POST'])
def sql_injection_flag():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        try:
            conn = get_db_connection()
            query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
            result = conn.execute(query).fetchone()
            conn.close()
            if result:
                return render_template('flag_2.html')  # Si la consulta es exitosa
        except Exception as e:
            return str(e), 500
    return render_template('sql_injection_flag.html')

# Reto Command Injection
@app.route('/command_injection_flag')
def command_injection_flag():
    command = request.args.get('cmd', '')
    if command:
        try:
            # Ejecutamos el comando recibido, pero de forma peligrosa
            command_output = os.popen(command).read()
            return render_template('flag_3.html', command_output=command_output)
        except Exception as e:
            return f"Error executing command: {str(e)}"
    return render_template('command_1.html', command_output="Try injecting a command in the URL.")

# Reto LFI
@app.route('/lfi_flag', methods=['GET'])
def lfi_flag():
    
    base_path = "files"
    requested_file = request.args.get('file', '')

    # Construir la ruta completa del archivo
    file_path = os.path.join(base_path, requested_file)

    # Imprimir la ruta para depuración (en Windows debería mostrar algo como C:\ruta\del\proyecto\files\flag.txt)
    #print(f"Ruta solicitada: {file_path}")
    #print(f"Ruta absoluta: {os.path.abspath(file_path)}")
    print(requested_file)

    # Validar que la ruta solicitada no salga del directorio base
    if not os.path.abspath(file_path).startswith(os.path.abspath(base_path)):
        return "<h1>Error:</h1><p>Acceso denegado.</p>", 403

    if requested_file == 'flag.txt':
        print(requested_file)
        try:
            with open(file_path, 'r') as f:
                content = f.read()
            return f"<h1>Contenido del archivo:</h1><pre>{content}</pre>"
        except FileNotFoundError:
            return "<h1>Error:</h1><p>El archivo solicitado no existe.</p>", 404
    return render_template('lfi_flag.html')
    
# Reto Broken Authentication
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Usar la función de autenticación con la base de datos
        if authenticate_user(username, password):
            session['user'] = username  # Guardar al usuario en la sesión
            return redirect(url_for('broken_authentication_flag'))
        else:
            return "Nombre de usuario o contraseña incorrectos.", 403

    return render_template('login.html')

# Ruta protegida que contiene la bandera
@app.route('/broken_authentication_flag')
def broken_authentication_flag():
    if 'user' not in session:
        return redirect(url_for('login'))

    return "<h1>¡Bandera encontrada! FLAG{BROKEN_AUTHENTICATION}</h1>"

# Reto CSRF
@app.route('/csrf_flag', methods=['GET', 'POST'])
def csrf_flag():
    if request.method == 'POST':
        # Token CSRF predecible (inseguro)
        if request.form.get('csrf_token') == "securetoken":
            return render_template('flag_5.html')  # Bandera encontrada
        return "CSRF token missing or invalid", 403
    return render_template('csrf_flag.html')  # Formulario visible para usuarios legítimos

# Reto IDOR


@app.route('/idor_flag', methods=['GET', 'POST'])
def idor_flag():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
        user = cursor.fetchone()

        conn.close()

        if user:
            session['user_id'] = user[0]  # Guardar el ID del usuario en la sesión
            #return redirect(url_for('idor_flag'))
        else:
            return "Nombre de usuario o contraseña incorrectos.", 403

    return render_template('idor_flag.html')

# Ruta protegida que contiene la bandera
@app.route('/idor_flag/<int:user_id>')
def idor_flag2(user_id):
    if 'user_id' not in session:
        return redirect(url_for('idor_flag'))

    # Si el usuario no tiene permisos para ver esta bandera
    if session['user_id'] != user_id:
        return "Acceso denegado. No tienes permiso para ver esta bandera.", 403

    return "<h1>¡Bandera encontrada! FLAG{IDOR_VULNERABILITY}</h1>"

@app.route('/logout')
def logout():
    # Eliminar la sesión del usuario
    session.clear()  # O puedes usar session.pop('user_id', None)

    # Redirigir al usuario a la página de inicio o a la página de login
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
