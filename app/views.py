
from crypt import methods
from fileinput import filename
from http.cookies import CookieError
from lib2to3.pgen2.pgen import DFAState
import os
from app import app

from flask import render_template, request, redirect, make_response, jsonify, abort, send_from_directory, session, url_for
from datetime import datetime

from werkzeug.utils import secure_filename

@app.template_filter('clean_date')
def date_filter(dt):
    return dt.strftime('%d %b %Y')

@app.route('/')
def index() -> str:
                                                            
    app.config['SECRET_KEY'] = 'SDFSDJFHK332'

    app.config['DB_USERNAME'] = 'root'

    print(app.config['DB_USERNAME'])

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

# @app.route('/sign-up', methods=["GET", "POST"])
# def sign_up():

#     if request.method == "POST":
#         req = request.form

#         username = req['username']
#         email = req.get('email')
#         password = req.get('password')
        
        

#         return redirect(request.url)

#     return render_template('sign-up.html')


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


# @app.route('/profile/<username>')
# def profile(username):

#     user = None
#     if username in users: 
#         user = users[username]

#     return render_template('profile.html', user=user)


@app.route('/json', methods=['POST'])
def json():

    if request.is_json:

        req = request.get_json()
        
        response = {
            'message': 'JSON recived',
            'name': req.get('name')
        }

        return make_response(jsonify(response)), 200

    else:

        return make_response(jsonify({'name': 'suck'})), 400

@app.route('/guestbook')
def guestbook():
    return render_template('guestbook.html')
    
@app.route('/guestbook/create_entry', methods=['POST'])
def create_entry():
    
    if request.is_json:

        req = request.get_json()

        print(req)

        return make_response(jsonify('Message have accepted')), 200

    else:

        return make_response(jsonify('Something went wrong')), 400

@app.route('/query')
def query():
    
    print(request.query_string())

    for k, v in request.args.items():
        print(k, v)

    return 'No query received', 200

app.config['IMAGE_UPLOADS'] = '/home/trtbfn/code/time-slicer/app/static/img'
app.config['ALLOWED_IMAGE_EXTENSIONS'] = ['JPG', 'PNG', 'JPEG', 'GIF']
app.config['MAX_IMAGE_FILESIZE'] = 0.5 * 1024 * 1024

def allowed_images(filename):

    if not '.' in filename:
        return False

    ext = filename.rsplit('.', 1)[1]
    
    if ext.upper() in app.config['ALLOWED_IMAGE_EXTENSIONS']:
        return True
    else: 
        return False

def allowed_image_filesize(filesize):
    
    if int(filesize) < app.config['MAX_IMAGE_FILESIZE']: 
        return True 
    else:
        return False

@app.route('/upload_image', methods=['GET', 'POST'])
def upload_image():

    if request.method == 'POST':
        
        if request.files:

            if not allowed_image_filesize(request.cookies.get('filesize')):
                print('File exceeded maximum size')
                return redirect(request.url)

            image = request.files['image']

            if image.filename == '':
                print("Name shouldn't be empty")

                return redirect(request.url)

            elif not allowed_images(image.filename):
                
                print('Image type is not allowed')

                return redirect(request.url)

            else:
                
                filename =  secure_filename(image.filename)
                image.save(os.path.join(app.config['IMAGE_UPLOADS'], filename))

                print('Image saved')

                return redirect(request.url)
    

    return  render_template('upload_image.html')


app.config['CLIENT_IMAGES'] = '/home/trtbfn/code/time-slicer/app/static/img'

@app.route('/get_image/<filename>')
def get_image(filename):
    
    try:
        return send_from_directory(app.config['CLIENT_IMAGES'], path=filename,as_attachment=False)
    except FileNotFoundError:
        abort(404)

@app.route('/cookies')
def cookies():

    cookies = request.cookies
    flavor = cookies.get('flavor')

    print(flavor)
    
    res = make_response('Cookies', 200)
    res.set_cookie('flavor',
                    value='chocolate chip',
                    max_age=20, 
                    path=request.path)

    return res


users = {
    'alexchico': {
        'username': 'Alex Shitenko',
        'bio': 'internship developer',
        'password': 'root'
    },
    'daffna': {
        'username': 'Daria Usefovich',
        'bio': 'Wirter, influencer',
        'password': 'root'
    }
}

@app.route('/sign-in', methods=['GET', 'POST'])
def sign_in():
    
    if request.method == 'POST':

        req = request.form

        user = req.get('username')
        password = req.get('password')

        if user in users:


            if not password == users[user]['password']:
                print("Password isn't correct")
                return redirect(request.url)

            else:
                session['USERNAME'] = user
                print('User added to session')
                return redirect(url_for('profile'))
        else:
            print("User isn't contained in users db")
            redirect(request.url)
            
    return render_template('sign-in.html')

@app.route('/sign-out')
def sign_out():
    
    session.pop('USERNAME', None)

    return redirect(url_for('sign_in'))


@app.route('/profile')
def profile():
    if session.get('USERNAME', None) is not None:  
        username = session.get('USERNAME')
        user = users[username]
        
        return render_template('profile.html', user=user)

    else:
        print('Username not found in session')
        return redirect(url_for('sign-in'))

from flask import flash

@app.route('/sign-up', methods=["GET", "POST"])
def sign_up():

    if request.method == "POST":
        req = request.form

        username = req['username']
        email = req.get('email')
        password = req.get('password')
        
        if not len(password) >= 10:
            flash('Password must be at least 10 characters in length', 'warning')
            return redirect(request.url)

        flash('Account have created', 'success')

        return redirect(request.url)

    return render_template('sign-up.html')