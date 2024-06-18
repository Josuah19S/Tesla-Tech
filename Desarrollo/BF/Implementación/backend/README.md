### TODO: Finish readme.md

### Leer antes de hacer pruebas
1. **Configuración inicial de `config.py`**:
   - No modifiques el archivo `config_sample.py`.
   - Crea una copia de `config_sample.py` y renómbrala a `config.py`.
     - Esto asegura que el programa funcione correctamente.
     - La información personal dentro de `config.py` será ignorada, ya que está incluida en el `.gitignore` del backend.

2. **Consultas y dudas**:
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
