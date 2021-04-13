from flask import Flask

app = Flask(__name__)

@app.route("/")
def home_view():
    return '<form action="#" method="post"><label for="firstname">First Name:</label><input type="text" id="firstname" name="fname" placeholder="firstname">
<label for="lastname">Last Name</label>
<input type="text" id="lastname" name="lname" placeholder="lastname">
<button type="submit">Login</button>'