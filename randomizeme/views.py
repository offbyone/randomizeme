from flask import render_template, redirect, url_for, session, request, current_app, flash

from randomizeme import app
from randomizeme.utils import twitter_factory, oauth
from randomizeme.decorators import login_required

twitter = twitter_factory(oauth)


@twitter.tokengetter
def get_twitter_oauth_token():
    return session.get('oauth_token')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login')
def login():
    url = url_for('.twitter_authorized', next=request.args.get('home') or request.referrer or None)
    resp = twitter.authorize(callback=url)
    return resp


@app.route('/twitter/authorized')
@twitter.authorized_handler
def twitter_authorized(resp):
    next_url = request.args.get('next') or url_for('.home')
    if resp is None:
        flash(u'You denied the request to sign in.')
        return redirect(next_url)

    session['twitter_token'] = (
        resp['oauth_token'],
        resp['oauth_token_secret']
    )
    session['twitter_user'] = resp['screen_name']
    current_app.logger.info(resp)
    flash('You were signed in as %s' % resp['screen_name'])
    return redirect(next_url)


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
