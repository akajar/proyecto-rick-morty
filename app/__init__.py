from flask import Flask
from flask_bootstrap import Bootstrap
from app.config import Config

def create_app():
    aplication = Flask(__name__)
    aplication.config.from_object(Config)
    Bootstrap(aplication)
    return aplication
