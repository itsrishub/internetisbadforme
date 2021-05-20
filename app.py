from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import cloudscraper
import requests
import json

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])
    
    @app.route("/", methods=['GET', 'POST'])
    def hello():
        form = ReusableForm(request.form)
    
        print(form.errors)
        if request.method == 'POST':
            name=request.form['name']
            print(name)
            scraper = cloudscraper.create_scraper()
            try:
                jsonGet = scraper.get(f"https://haveibeenpwned.com/unifiedsearch/{name}").text
                jsonData = json.loads(jsonGet)
                if jsonData['Breaches']:
                	site = ""
                	flash("Oh no - Your data have been breached!")

                	for data in jsonData['Breaches']:
                		site = data['Title']
                		# if data['Title']:
                		flash(data['Title'])
                		# else:
                		# 	print("Your email is safe!")
                		# 	break

                else:
                	print("You are safe!")
            except:
            	flash("Your are safe!")

            
    
        if form.validate():
            # Save the comment here.
            print("nth")
        else:
            flash('All the form fields are required. ')
        return render_template('main.html', form=form)

if __name__ == "__main__":
    app.run()
