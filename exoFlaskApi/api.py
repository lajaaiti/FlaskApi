#import flask
from flask import Flask, request, jsonify

# creation de l'application
app = Flask(__name__)

# définition de la route
@app.route('/')
def index():
    return "Hello World !"

