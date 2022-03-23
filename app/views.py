
from cgitb import html
import email
from webbrowser import get
from app import app

from flask import render_template, request, redirect
from datetime import datetime

@app.template_filter('clean_date')
def date_filter(dt):
    return dt.strftime('%d %b %Y')

@app.route('/')
def index() -> str:
    return render_template('index.html')

@app.route('/about')
def about() -> str:
    return render_template('about.html')

@app.route('/conditions')
def conditions():

    languages = [
        'C', 'Python', 'JavaScript',
        'C#'
    ]

    val = 32

    employees = {
        'James': 32,
        'Ann': 23,
        'Noe': 33,
        'Kiba': 43,
        'Jinjer': 26
    }

    threshold = 89

    date = datetime.utcnow()

    class Person:
        def __init__(self, name, age) -> None:
            self.name = name
            self.age = age

    person = Person('Jane', 32)

    props = ('small', 'large')

    def say_out_load(sentance: str, num: int) -> str:
        return (sentance + ' ') * num

    script = '<script>alert("You have been hached")</script>'

    html_text = '<span>Oh, your system have been crushed:(</span>'

    return render_template(
        'conditions.html', 
        val=val, 
        languages=languages,
        employees=employees,
        person=person, 
        say_out_load=say_out_load,
        props=props,
        threshold=threshold,
        date=date,
        script=script,
        html_text=html_text)

@app.route('/sign-up', methods=["GET", "POST"])
def sign_up():

    if request.method == "POST":
        req = request.form

        username = req['username']
        email = req.get('email')
        password = req.get('password')
        
        

        return redirect(request.url)

    return render_template('sign-up.html')


users = {
    'alexchico': {
        'name': 'Alex Shitenko',
        'bio': 'internship developer'
    },
    'daffna': {
        'name': 'Daria Usefovich',
        'bio': 'Wirter, influencer'
    }
}


@app.route('/profile/<username>')
def profile(username):

    user = None
    if username in users: 
        user = users[username]

    return render_template('profile.html', user=user)