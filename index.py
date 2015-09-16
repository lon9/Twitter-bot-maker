# -*- coding: utf-8 -*-

from app import app
from bottle import run
from beaker.middleware import SessionMiddleware
session_opts = {
		'session.type': 'file',
		'session.data_dir': './lock',
		'session.cookie_expires': True,
		'session.auto': True
		}
app = SessionMiddleware(app, session_opts)
run(app, host='localhost', port=8080, debug=True, reloader=True)

