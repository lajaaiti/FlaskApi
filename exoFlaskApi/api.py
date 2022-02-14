#import flask
from email.mime import application
from flask import Flask, template_rendered

# creation de l'application
app = Flask(__name__)

# définition de la route
@app.route('/')
def home():
    return ("coucouc.!")

# instancier un scraper
@app.route('/scraper')
def scraper():
    return ("scraper")


# run application
app.run(debug=True)
    
    

