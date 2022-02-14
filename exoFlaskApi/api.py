#import flask
from flask import Flask, template_rendered

# creation de l'application
app = Flask(__name__)

# définition de la route
@app.route('/')
def home():
    return template_rendered('index.html')



    
    

