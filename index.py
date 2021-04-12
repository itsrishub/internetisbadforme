from flask import Flask
import cloudscrapper
import requests
import json
app = Flask(__name__)

@app.route('/')
def hello_world():
  print("hello")
