from app import app

from flask import render_template

@app.route('/')
def index() -> str:
    return render_template('index.html')

@app.route('/about')
def about() -> str:
    return render_template('about.html')
