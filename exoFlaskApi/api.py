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

# creation de l'application
app = Flask(__name__)

# définition de la route home
@app.route('/')
def home():
    return ("Hello World!")

# instancier une bdd sqlite 
db = sqlite3.connect('database.db')


# création d'une table text et user avec sql alchemy
class Text(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))
    def __init__(self, text):
        self.text = text
        


# webscrapping avec bs4
url = "http://feeds.bbci.co.uk/news/rss.xml"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser") 
items = soup.find_all("item")
item = items[0]
item.title.text
item.description.text
item.pubDate.text
item.link.text
 










# run application
if __name__ == "__main__":
    app.run(debug=True)

    
    

