from app import app
from flask import render_template

@app.route('/admin')
def admin_home() -> str:
    return render_template('admin_index.html')


