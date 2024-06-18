from flask import Flask, jsonify
from flask_mysqldb import MySQL
import config

app = Flask(__name__)

# Configuración de la conexión a la base de datos
app.config['MYSQL_HOST'] = config.MYSQL_HOST
app.config['MYSQL_USER'] = config.MYSQL_USER
app.config['MYSQL_PASSWORD'] = config.MYSQL_PASSWORD
app.config['MYSQL_DB'] = config.MYSQL_DB

mysql = MySQL(app)

# Configuracion de acceso a tablas
table_access = ['alumnos','administradores','libros']

def has_access(table_name):
    try:
        table_access.index(table_name)
        return True
    except Exception as e:
        print(f'{type(e)}: {e}')
        return False

# Rutas de la API
@app.route('/api/')
def specify_table_error():
    return jsonify({'error':'You must specify a table in \'api/\'!'})

@app.route('/api/<tabla>')
def get_access_table_data(tabla):
    try:

        if has_access(tabla):
            cur = mysql.connection.cursor()
            cur.execute(f'''SELECT * FROM {tabla}''')
            results = cur.fetchall()
        else:
            results = {"message": "You have no access to that table! (or maybe it just not exist...)"}

        return jsonify(results)
    
    except Exception as e:
        return str(e)

# Run app
if __name__ == '__main__':
    app.run(debug=True)
