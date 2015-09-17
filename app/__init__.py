# -*- coding:utf-8 -*-
__version = '1.0'
from bottle import Bottle, TEMPLATE_PATH
app = Bottle()
TEMPLATE_PATH.append("./app/views")
TEMPLATE_PATH.remove("./views/")
from app.controllers import *
