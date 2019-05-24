import multiprocessing

import gunicorn
from gevent import monkey

monkey.patch_all()

bind = '0.0.0.0:8000'
worker_class = 'gevent'
workers = multiprocessing.cpu_count() * 2 + 1
loglevel = 'debug'
keepalive = 10
timeout = 3600
preload_app = True

gunicorn.SERVER_SOFTWARE = 'Microsoft-IIS/6.0'
