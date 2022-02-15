#import flask
from email.mime import application
from unicodedata import name
from urllib import response
from flask import Flask, template_rendered, request, render_template, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
import json
import sqlite3
import requests
# import la class Model
import Model.model as model
# import beautifulsoup4
from bs4 import BeautifulSoup
import pandas as pd

# creation de l'application
app = Flask(__name__)

# définition de la route home
@app.route('/')
def home():
    return ("Hello World!")



# run application
if __name__ == "__main__":
    app.run(debug=True)

    
    

