from flask import Flask
import cloudscraper
import requests
import json

app = Flask(__name__)

@app.route("/")
def home_view():
	print("hello bsdk")
