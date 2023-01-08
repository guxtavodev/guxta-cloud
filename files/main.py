from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
#from api.index import API
import sqlite3 as sql
from models import Newsletter, User, db

# Criando a aplicação
app = Flask(__name__, template_folder="front-end")

from routes import *

if __name__ == "__main__":
	app.run(host="0.0.0.0")

