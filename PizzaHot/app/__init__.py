"""App config"""

# Standard libraries
import os

# Flask
from flask import Flask

# Third party libraries
from dotenv import load_dotenv


# App config
app = Flask(__name__)

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Secret key
app.secret_key = os.getenv("SECRET_KEY")

# Configuración para subir una imagen
UPLOAD_FOLDER = str(app.static_folder) + "/uploads"
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS'] = ALLOWED_EXTENSIONS
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
