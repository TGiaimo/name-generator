from flask import render_template
from app import app
from app import name_generator

@app.route('/')
@app.route('/index')
def index():
    titles = name_generator.generate(1)
    return render_template('index.html', titles=titles)