from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcome():
   """Return welcome greeting"""
   return "welcome"

@app.route('/welcome/home')
def welcome_home():
   """Return welcome home greeting"""
   return "welcome home"

@app.route('/welcome/back')
def welcome_back():
   """Return welcome back greeting"""
   return "welcome back"