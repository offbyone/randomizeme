from flask_oauth import OAuth
oauth = OAuth()

from randomizeme import app


def _dot_lookup(thing, comp, import_path):
    try:
        return getattr(thing, comp)
    except AttributeError:
        __import__(import_path)
        return getattr(thing, comp)


def importer(target):
    components = target.split('.')
    import_path = components.pop(0)
    thing = __import__(import_path)

    for comp in components:
        import_path += ".%s" % comp
        thing = _dot_lookup(thing, comp, import_path)
    return thing


class ConfigurationMethodDelegator(object):

    def __init__(self, config_key, default_method=None):
        self.config_key = config_key
        self.default_method = default_method

    def __call__(self, *a, **kw):
        return self.delegate(*a, **kw)

    @property
    def delegate(self):
        if hasattr(self, '_delegate') and self._delegate is not None:
            return self._delegate

        try:
            config_method_name = app.config[self.config_key]
            config_method = importer(config_method_name)
        except (KeyError, ImportError, AttributeError):
            config_method = self.default_method

        self._delegate = config_method
        return self._delegate


def twitter_factory(oauth):
    return oauth.remote_app('twitter',
                            base_url='https://api.twitter.com/1/',
                            request_token_url='https://api.twitter.com/oauth/request_token',
                            access_token_url='https://api.twitter.com/oauth/access_token',
                            authorize_url='https://api.twitter.com/oauth/authenticate',
                            consumer_key=app.config['TWITTER_OAUTH_CONSUMER_KEY'],
                            consumer_secret=app.config['TWITTER_OAUTH_CONSUMER_SECRET'],
                            )
