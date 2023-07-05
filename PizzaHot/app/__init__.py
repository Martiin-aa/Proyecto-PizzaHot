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
