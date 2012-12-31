from flask import session

from flask.ext.security import Security, SQLAlchemyUserDatastore

from flask.ext.social import Social
from flask.ext.social.datastore import SQLAlchemyConnectionDatastore
from flask.ext.social import login_failed
from flask.ext.social.utils import get_conection_values_from_oauth_response

from flask.ext.bootstrap import Bootstrap

from randomizeme import app, db
from . import data

Bootstrap(app)

user_datastore = SQLAlchemyUserDatastore(db, data.User, data.Role)
security = Security(app, user_datastore)
social = Social(app, SQLAlchemyConnectionDatastore(db, data.Connection))


class SocialLoginError(Exception):
    def __init__(self, provider):
        self.provider = provider


@login_failed.connect_via(app)
def on_login_failed(sender, provider, oauth_response):
    app.logger.debug('Social Login Failed via %s; '
                     '&oauth_response=%s' % (provider.name, oauth_response))

    # Save the oauth response in the session so we can make the connection
    # later after the user possibly registers
    session['failed_login_connection'] = \
        get_conection_values_from_oauth_response(provider, oauth_response)

    raise SocialLoginError(provider)


# connection_created.connect(connect_new_user)
