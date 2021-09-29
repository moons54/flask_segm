from flask import Flask
myapp = Flask(__name__)

@myapp.route("/")
def hello():
    return  render_template('template/home.html')
    #return "Hello Flask, on Azure App to number 1"
