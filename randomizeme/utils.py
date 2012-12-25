from flask_oauth import OAuth
oauth = OAuth()

from randomizeme import app

def twitter_factory(oauth):
    return oauth.remote_app('twitter',
                            base_url='https://api.twitter.com/1/',
                            request_token_url='https://api.twitter.com/oauth/request_token',
                            access_token_url='https://api.twitter.com/oauth/access_token',
                            authorize_url='https://api.twitter.com/oauth/authenticate',
                            consumer_key=app.config['TWITTER_OAUTH_CONSUMER_KEY'],
                            consumer_secret=app.config['TWITTER_OAUTH_CONSUMER_SECRET'],
                            )
