from flask import Flask
import cloudscraper
import requests
import json

app = Flask(__name__)

@app.route("/")
def home_view():
	email = input("Enter email\n\n")

	scraper = cloudscraper.create_scraper()
	jsonGet = scraper.get(f"https://haveibeenpwned.com/unifiedsearch/{email}").text
	jsonData = json.loads(jsonGet)

	site = ""

	for data in jsonData['Breaches']:
		site = data['Title']
		if data['Title']:
			print(data['Title'])
		else:
			print("Your email isn't breached!")
			break

	input("\n\n\n\nenter to exit...")
