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
# webscrapping avec bs4
url = "http://feeds.bbci.co.uk/news/rss.xml"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser") 
items = soup.findAll("item")
item = items[0]
item.title.text 
item.description.text
item.pubDate.text

news_items = []
for i in items:
    news_i = {}
    news_i["title"] = i.title.text
    news_i["description"] = i.description.text
    news_i["pubDate"] = i.pubDate.text
    news_items.append(news_i)
    
df = pd.DataFrame(news_items, columns=["title", "description", "pubDate"])
df.to_csv("news.csv", index=False)
   
    
 










# run application
if __name__ == "__main__":
    app.run(debug=True)

    
    

