#import flask
from email.mime import application
from flask import Flask, template_rendered, request, render_template, redirect, url_for, flash, jsonify
import json
import sqlite3

# creation de l'application
app = Flask(__name__)

# définition de la route home
@app.route('/')
def home():
    return ("Hello World!")

# instancier une bdd sqlite 
db = sqlite3.connect('database.db')




# run application
if __name__ == "__main__":
    app.run(debug=True)

    
    

