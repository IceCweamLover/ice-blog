from flask import Flask
from flask import render_template
from flask import request
import requests



app=Flask(__name__)

@app.route('/')
def about():
  return render_template('about.html')

@app.route('/blog')
def about():
  return render_temlpate('blog.html')
  
if __name__=="__main__":
  app.run()
