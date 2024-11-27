FROM python:3.9-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar el archivo requirements.txt e instalar dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de la aplicación
COPY . .

# Crear el archivo de base de datos
# RUN python init_db.py

# Exponer el puerto
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
