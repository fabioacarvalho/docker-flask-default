from flask import Flask
import os
from importlib import import_module
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

load_dotenv()


USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
SERVER = os.getenv("SERVER")
DB = os.getenv("DB")

# Rota com as configurações para acesso ao banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


# Import all views from setup.views
current_directory = os.path.join(os.path.dirname(__file__), 'views')
for filename in os.listdir(current_directory):
    if filename.endswith("_view.py"):
        filepath = os.path.join(current_directory, filename)
        with open(filepath) as f:
            code = f.read()
            exec(code, globals())
