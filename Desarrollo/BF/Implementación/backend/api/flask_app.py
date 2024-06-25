import os
from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
import pandas as pd
import config

app = Flask(__name__)

# Configuración de la conexión a la base de datos (esto es una prueba)
app.config['MYSQL_HOST'] = config.MYSQL_HOST
app.config['MYSQL_USER'] = config.MYSQL_USER
app.config['MYSQL_PASSWORD'] = config.MYSQL_PASSWORD
app.config['MYSQL_DB'] = config.MYSQL_DB

mysql = MySQL(app)

# ============================================================
# Rutas

file_path = os.path.dirname(__file__)
data_path = '../database/data/'

# Ruta para cargar datos desde el archivo CSV a la base de datos
@app.route('/api/insertar/alumnos', methods=['GET'])
def insertar_alumnos():
    try:
        csv_path = os.path.join(file_path, data_path, 'alumnos.csv')

        # Cargar el archivo CSV en un DataFrame de Pandas
        df = pd.read_csv(csv_path, delimiter='\t', encoding='utf-8')

        # Conexión al cursor de la base de datos
        cur = mysql.connection.cursor()

        # Iterar sobre cada fila del DataFrame e insertar en la base de datos
        for index, row in df.iterrows():
            # Obtener los valores de cada columna
            cod_alumno = row['cod_alumno']
            nombres = row['nombres']
            apellidos = row['apellidos']
            escuela_prof = row['escuela_prof']

            # Ejecutar la consulta SQL para insertar en la tabla alumnos
            cur.execute("INSERT INTO alumnos (cod_alumno, nombres, apellidos, escuela_prof) VALUES (%s, %s, %s, %s)",
                        (cod_alumno, nombres, apellidos, escuela_prof))

        # Confirmar los cambios en la base de datos
        mysql.connection.commit()

        # Cerrar cursor
        cur.close()

        return 'ALUMNOS cargados correctamente en la base de datos.'

    except Exception as e:
        return f'Error al cargar los datos de ALUMNOS: {str(e)}'

# Ruta para cargar datos de administradores desde el archivo CSV a la base de datos
@app.route('/api/insertar/admins', methods=['GET'])
def insertar_admins():
    try:
        csv_path = os.path.join(file_path, data_path, 'administradores.csv')

        # Cargar el archivo CSV en un DataFrame de Pandas
        df = pd.read_csv(csv_path, delimiter='\t', encoding='utf-8')

        # Conexión al cursor de la base de datos
        cur = mysql.connection.cursor()

        # Iterar sobre cada fila del DataFrame e insertar en la base de datos
        for index, row in df.iterrows():
            # Obtener los valores de cada columna
            cod_admin = row['cod_admin']
            nombres = row['nombres']
            apellidos = row['apellidos']
            cargo = row['cargo']

            # Ejecutar la consulta SQL para insertar en la tabla administradores
            cur.execute("INSERT INTO administradores (cod_admin, nombres, apellidos, cargo) VALUES (%s, %s, %s, %s)",
                        (cod_admin, nombres, apellidos, cargo))

        # Confirmar los cambios en la base de datos
        mysql.connection.commit()

        # Cerrar cursor
        cur.close()

        return 'ADMINISTRADORES cargados correctamente en la base de datos.'

    except Exception as e:
        return f'Error al cargar los datos de ADMINISTRADORES: {str(e)}'

# Ruta para insertar usuarios
@app.route('/api/insertar/usuarios', methods=['GET'])
def insertar_usuarios():
    try:
        csv_path = os.path.join(file_path, data_path, 'usuarios.csv')

        # Cargar el archivo CSV en un DataFrame de Pandas
        df = pd.read_csv(csv_path, delimiter='\t', encoding='utf-8')

        # Conexión al cursor de la base de datos
        cur = mysql.connection.cursor()

        # Iterar sobre cada fila del DataFrame e insertar en la base de datos
        for index, row in df.iterrows():
            # Obtener los valores de cada columna para usuarios/administradores
            id_usuario = row['id_usuario']
            cod_admin = row['cod_admin']
            cod_alumno = row['cod_alumno']
            username = row['username']
            password = row['password']
            rol = row['rol']

            # Verificar si es un administrador o un usuario
            if pd.notna(cod_admin):
                # Es un administrador
                cur.execute("INSERT INTO usuarios_sist (id_usuario, cod_admin, username, password, rol) "
                            "VALUES (%s, %s, %s, %s, %s)",
                            (id_usuario, cod_admin, username, password, rol))
            elif pd.notna(cod_alumno):
                # Es un alumno
                cur.execute("INSERT INTO usuarios_sist (id_usuario, cod_alumno, username, password, rol) "
                            "VALUES (%s, %s, %s, %s, %s)",
                            (id_usuario, cod_alumno, username, password, rol))

        # Confirmar los cambios en la base de datos
        mysql.connection.commit()

        # Cerrar cursor
        cur.close()

        return 'Datos de USUARIOS cargados correctamente en la base de datos.'

    except Exception as e:
        return f'Error al cargar los datos de USUARIOS: {str(e)}'

# Ruta para autenticación de usuarios
@app.route('/api/login', methods=['POST'])
def login():
    # Obtener datos del formulario
    username = request.json.get('username')
    password = request.json.get('password')

    # Validar que se recibieron el usuario y contraseña
    if not username or not password:
        return jsonify({'message': 'Se requiere usuario y contraseña'}), 400

    # Conexión al cursor de la base de datos
    cur = mysql.connection.cursor()

    try:
        # Consultar si el usuario existe en la base de datos
        cur.execute("SELECT id_usuario, cod_admin, cod_alumno, username, password, rol FROM usuarios_sist WHERE username = %s", (username,))
        usuario = cur.fetchone()

        if not usuario:
            return jsonify({'message': 'Credenciales incorrectas'}), 401

        # Verificar la contraseña
        stored_password = usuario[4]
        if password == stored_password:
            # Contraseña válida, determinar tipo de usuario
            return jsonify({
                'message': 'Autenticación exitosa',
                'username': usuario[3],
                'rol': usuario[5]
            }), 200
        else:
            # Contraseña incorrecta
            return jsonify({'message': 'Credenciales incorrectas'}), 401

    except Exception as e:
        return jsonify({'message': f'Error en la autenticación: {str(e)}'}), 500

    finally:
        # Cerrar cursor
        cur.close()

# ============================================================

# Run app
if __name__ == '__main__':
    app.run(debug=True)
