#import flask
from email.mime import application
from flask import Flask, template_rendered

# creation de l'application
app = Flask(__name__)

# définition de la route
@app.route('/')
def home():
    return template_rendered('index.html')

# run application
app.run(debug=True)
    
    

