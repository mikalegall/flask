import sys
assert sys.version_info.major >= 3

sys.path.insert(0, '/home/flaskwsgi/public_wsgi/')
from app import app as application