from flask import Flask
from flask import render_template

app = Flask(__name__)
@app.route("/")
def index():
  number = [i for i in range(1,11)]
  return render_template("squares.html",len=len(number),data = number)
  
  