from logging import root
from flask import Flask, render_template


# creation de l'application
app = Flask(__name__)

@app.route('/')
def home():
    return ("Hello World!")
