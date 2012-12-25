import os

from flask import Flask
from flask.ext.bootstrap import Bootstrap


class DefaultConfig(object):
    TWITTER_OAUTH_CONSUMER_KEY = None
    TWITTER_OAUTH_CONSUMER_SECRET = None
    # this must be changed for deployment
    SECRET_KEY = "l\x96\x9c9\xfa08DTT\xb6\x1d,\xbda\x02\x9b\x85\xf3\xff1\xf5\xb1\xaa"

app = Flask(__name__)
app.config.from_object('randomizeme:DefaultConfig')
if 'RANDOMIZEME_SETTINGS' in os.environ:
    app.config.from_envvar('RANDOMIZEME_SETTINGS')
Bootstrap(app)

app.secret_key = app.config.SECRET_KEY

import randomizeme.views
