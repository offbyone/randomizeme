from flask import render_template

from randomizeme import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload-library')
def upload_library():
    pass

@app.route('/submit-playlist')
def submit_playlist():
    pass

@app.route('/get-playlist')
def get_playlist():
    pass

@app.route('/library/{user}')
def user_library(user):
    pass

@app.route('/manage-library')
def my_libraries():
    pass
