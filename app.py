from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_library.db'
app.config['SECRET_KEY'] = 'ssshh_secret'

db = SQLAlchemy(app)

@app.route('/')
@app.route('/home')
def home():
    return render_template('welcome.html')

@app.errorhandler(404)
def not_found(e):
    return render_template('not_found_404.html')

import routes

