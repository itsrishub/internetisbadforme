



from flask import Flask
import cloudscrapper
import requests
import json
app = Flask(__name__)

@app.route('/')
def hello_world():
  email = input("Enter your email\n\n")

  scraper = cloudscraper.create_scraper()
  jsonGet = scraper.get(f"https://haveibeenpwned.com/unifiedsearch/{email}").text
  jsonData = json.loads(jsonGet)

  site = ""

  for data in jsonData['Breaches']:
    site = data['Title']
    if data['Title']:
      print(data['Title'])
     else:
      print("Your email is safe!\n\n")
      break
   input("\nEnter to exit\n")
