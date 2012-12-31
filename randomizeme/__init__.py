import os

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

class DefaultConfig(object):
    TWITTER_OAUTH_CONSUMER_KEY = None
    TWITTER_OAUTH_CONSUMER_SECRET = None
    BOOTSTRAP_CSS = "css/bootstrap-superhero.css"
    SECURITY_REGISTERABLE = True

    # this must be changed for deployment, in the file referenced by RANDOMIZEME_SETTINGS
    SECRET_KEY = "l\x96\x9c9\xfa08DTT\xb6\x1d,\xbda\x02\x9b\x85\xf3\xff1\xf5\xb1\xaa"

app = Flask(__name__)
app.config.from_object('randomizeme:DefaultConfig')
if 'RANDOMIZEME_SETTINGS' in os.environ:
    app.config.from_envvar('RANDOMIZEME_SETTINGS')

app.secret_key = app.config['SECRET_KEY']
# from pprint import pprint; pprint(dict(app.config)) # flake8: noqa

db = SQLAlchemy(app)

import randomizeme.infrastructure # flake8: noqa
import randomizeme.views # flake8: noqa
from randomizeme import data # flake8: noqa
