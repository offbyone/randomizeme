from flask import render_template, redirect, url_for, session, request, current_app, flash
from flask_security.decorators import login_required
from randomizeme import app
from randomizeme.infrastructure import social, SocialLoginError


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html',
                           twitter_conn=social.twitter.get_connection(),
                           facebook_conn=social.facebook.get_connection(),
                           foursquare_conn=social.foursquare.get_connection())


@app.route('/logout')
def logout():
    session.pop('twitter_user')
    return redirect(request.args.get('next') or url_for('.home'))


@app.route('/upload-library')
@login_required
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


@app.errorhandler(SocialLoginError)
def social_login_error(error):
    return redirect(
        url_for('security.register', provider_id=error.provider.id, login_failed=1))
