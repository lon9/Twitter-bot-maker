# -*- coding:utf-8 -*-

from app import app
from bottle import static_file

@app.route('/static/<filepath:path>')
def server_static(filepath):
	return static_file(filepath, root="app/static/")
