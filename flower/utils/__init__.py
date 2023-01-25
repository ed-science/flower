import uuid
import base64
import os.path

from .. import __version__


def gen_cookie_secret():
    return base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes)


def bugreport(app=None):
    try:
        import celery
        import tornado
        import humanize

        app = app or celery.Celery()

        return f"flower   -> flower:{__version__} tornado:{tornado.version} humanize:{getattr(humanize, '__version__', None) or getattr(humanize, 'VERSION')}{app.bugreport()}"
    except (ImportError, AttributeError) as e:
        return f"Error when generating bug report: {e}. Have you installed correct versions of Flower's dependencies?"


def abs_path(path):
    path = os.path.expanduser(path)
    if not os.path.isabs(path):
        cwd = os.environ.get('PWD') or os.getcwd()
        path = os.path.join(cwd, path)
    return path


def prepend_url(url, prefix):
    return '/' + prefix.strip('/') + url
