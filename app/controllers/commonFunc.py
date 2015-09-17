# -*- coding:utf-8 -*-

# Generate random strings
def getRandomStr(length, chars=None):
	import random
	import string
	if chars is None:
		chars = string.digits + string.ascii_letters
	return ''.join([random.choice(chars) for i in range(length)])
