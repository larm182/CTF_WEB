#!/usr/bin/python
#-*- coding: utf-8 -*-
#Autor: Luis Angel Ramirez Mendoza

import sqlite3

def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Crear la tabla 'users'
    cursor.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL, password TEXT NOT NULL)''')

    # Insertar datos de prueba
    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', ('admin', 'admin123'))
    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', ('test', 'test123'))

    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
    print("Base de datos inicializada.")