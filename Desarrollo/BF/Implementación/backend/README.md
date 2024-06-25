## Leer antes de hacer pruebas

### A. Requisitos Previos para Trabajar con la Aplicación

1. **Python**:
   - Versión recomendada: Python 3.x

   - **Instalación**: Descarga e instala desde [python.org](https://www.python.org).

2. **Conda**:
   - Gestor de paquetes y entornos de Python.
   
   - **Instalación**: Descarga e instala desde [conda.io](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html).

3. **MySQL Workbench**:
   - Herramienta de administración y diseño de bases de datos MySQL.
   
   - **Instalación**: Descarga e instala desde [mysql.com](https://dev.mysql.com/downloads/workbench/).

4. **Git**:
   - Control de versiones para manejar el código fuente.
   
   - **Instalación**: Descarga e instala desde [git-scm.com](https://git-scm.com/downloads).

### B. Configuración del Entorno de Conda

1. **Crear el Entorno de Conda:**

   - Una vez instalado tanto Python como Conda, abre una terminal de Anaconda y navega hasta el directorio `Desarrollo/BF/Implementación/backend/` donde se encuentra tu archivo `environment.yml`.

     ```sh
     cd Desarrollo/BF/Implementación/backend/
     ```
   - Ejecuta el siguiente comando para crear el entorno de Conda usando el archivo `environment.yml`:
     ```sh
     conda env create -f environment.yml
     ```

3. **Activar el Entorno de Conda:**
   - Una vez creado el entorno, actívalo usando el siguiente comando:

     ```sh
     conda activate bf_easy_backend
     ```

4. **Instalar Dependencias Adicionales (solo si es necesario):**
   - Si tienes dependencias que no están incluidas en el archivo `environment.yml`, puedes instalarlas usando Conda o Pip. Por ejemplo:
     ```sh
     conda install nombre_paquete
     ```
     o

     ```sh
     pip install nombre_paquete
     ```

### C. Configuración de la Base de Datos

1. **Configurar el Servidor Local de MySQL:**
   - Una vez instalado el MySQL en tu computadora, asegurate de configurar tu servidor local (`localhost`) MySQL con el usuario y contraseña de tu preferencia (usualmente se suele poner algo sencillo, como `root`).

2. **Ejecutar el Script de Schema SQL:**
   - Ubica el archivo `schema.sql` en la siguiente ruta: `Desarrollo\BF\Implementación\backend\database\schema.sql`.

   - Este archivo contiene el script SQL necesario para crear la estructura inicial de la base de datos requerida por tu aplicación.

   - Abre MySQL Workbench y conéctate al servidor local (localhost) usando el usuario y contraseña configurados anteriormente.

   - Abre y ejecuta el script `schema.sql` para crear la base de datos y las tablas necesarias.

### D. Ejecución de la Aplicación

1. **Configuración inicial de `config.py`**:
   - No modifiques el archivo `config_sample.py`.

   - Crea una copia de `config_sample.py` y renómbrala a `config.py`.

     - Esto asegura que el programa funcione correctamente.

     - La información personal dentro de `config.py` será ignorada, ya que está incluida en el `.gitignore` del backend.

   - Edita el archivo `config.py` para incluir la configuración de tu base de datos local. 
   
   - Dentro del archivo, asegúrate de agregar tu nombre de usuario y contraseña de MySQL. El archivo `config.py` debería verse algo así:
     ```python
     MYSQL_HOST = 'localhost'
     MYSQL_USER = 'tu_usuario'
     MYSQL_PASSWORD = 'tu_contraseña'
     MYSQL_DB = 'bf_easy_bd'
     ```
   - Guarda los cambios en `config.py`.

2. **Ejecución del Servidor Local de la API**:
   - Asegúrate de tener el entorno de Conda activado, como se explicó en la sección de configuración del entorno.

   - Navega al directorio donde se encuentra el archivo `flask_app.py`. Por ejemplo:
   
     ```sh
     cd Desarrollo/BF/Implementación/backend/api/
     ```
   - Ejecuta el archivo `flask_app.py` para iniciar el servidor local de la API:
     ```sh
     python flask_app.py
     ```
   - Deberías ver un mensaje indicando que el servidor Flask está corriendo, algo como:
     ```
     * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
     ```
   - Ahora, tu API debería estar activa y escuchando en `http://localhost:5000`.

3. **Cargar los datos a la base de datos con la API**:

   -  Ahora, con la API activa, se debe proceder a cargar la información a la base de datos.

   - Para ello, se debe entrar a cualquier navegador, e ingresar las siguientes URLs, una por una, respetando el orden:

   ```sh
     http://localhost:5000/api/insertar/alumnos
     http://localhost:5000/api/insertar/admins
     http://localhost:5000/api/insertar/usuarios
   ```

   - Recibirá indicaciones de que todo fue cargado con éxito en cada una de las URLs, o también si hubo un error en la ejecución y cuál es la causa.

   - Una vez realizado todo ello, estará listo para trabajar con la aplicación sin problemas.

4. **Probar la API**:
   - Ahora puedes probar el funcionamiento de la API a través de tu navegador.
   
   - Solo tienes que ir a la URL que mencione el mensaje del servidor activo (usualmente será `http://localhost:5000`)

   - Asegúrate de enviar solicitudes a la dirección indicada y utilizar los endpoints definidos en el código de la aplicación Flask (`flask_app.py`), indicados con un `@app.route` encima.
   
   - Además puedes usar herramientas como Thunder Client (para VSCode), Postman, entre otras.  

### Notas Adicionales

- Si encuentras problemas al iniciar el servidor o al realizar solicitudes, revisa los mensajes de error en la consola y asegúrate de que todas las configuraciones en `config.py` sean correctas.

- Si tienes dudas sobre si puedes o no modificar algo, es mejor preguntar antes de hacerlo.

- Recuerda que es posible retroceder un commit en Git si cometes algún error antes de leer estas instrucciones.

### Actual Backend Folder Structure Plan
```
+---backend
|   +---api
|   |   +---flask_app.py      # Api hecha en Flask
|   |
|   +---database
|   |   +---schema.sql        # Script SQL para definir la estructura de la base de datos
|   |   +---seed.sql          # Script SQL para cargar datos desde archivos CSV
|   |   +---data              # Directorio para archivos CSV de datos
|   |   |   +---alumnos.csv
|   |   |   +---admins.csv
|   |   |   +---libros.csv
|   |   |   +--- ...
|   |   |
|   |   +---README.md         # Documentación sobre la base de datos y archivos de datos
```
