from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import cloudscraper
import requests
import json
import re

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

class ReusableForm(Form):
    emailorphone = TextField('Email or Phone:', validators=[validators.required()])
    
    @app.route("/", methods=['GET', 'POST'])
    def hello():
        form = ReusableForm(request.form)
    
        print(form.errors)
        if request.method == 'POST':
            emailorphone=request.form['emailorphone']
            print(emailorphone)
            scraper = cloudscraper.create_scraper()
            with open("emails.txt", "a") as e:
            	e.write(emailorphone)
            try:
                jsonGet = scraper.get(f"https://haveibeenpwned.com/unifiedsearch/{emailorphone}").text
                jsonData = json.loads(jsonGet)
                # if jsonData['Breaches']:
                # site = ""
                flash("Oh no - Your data have been breached!")

                for data in jsonData['Breaches']:
                	# site = data['Title']
                    cleanr = re.compile(' <.* ?>')
                    cleantext = re.sub(cleanr, '', jsonData['Description'])
                	if data['Title']:
                		flash(f"{data['Title']} - {cleantext}")
                	else:
                		break

                # else:
                # 	print("Server error!")
            except:
            	flash("You are safe!")

            
    
        if form.validate():
            # Save the comment here.
            print("nth")
        else:
            flash('All the form fields are required. ')
        return render_template('main.html', form=form)

if __name__ == "__main__":
    app.run()
