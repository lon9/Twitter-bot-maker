# -*- coding:utf-8 -*-

from app import app
from bottle import route, request, redirect, static_file, jinja2_template as template
import tweepy
from app.controllers import commonFunc as common
import os

@app.route('/', method='GET')
def index():
	isFail = False
	if 'failure' in request.query:
		if request.query.failure == "True":
			isFail=True
	return template('index', isFail=isFail)

@app.route('/login', method='POST')
def login():
	session = request.environ.get('beaker.session')
	if not request.forms.get('consumerKey') or not request.forms.get('consumerSecret'):
		redirect('/?failure=True')
	consumerKey = request.forms.get('consumerKey')
	consumerSecret = request.forms.get('consumerSecret')
	tweetsFile = request.files.get('tweetsFile')
	name, ext = os.path.splitext(tweetsFile.filename)
	if not ext =='.txt':
		redirect('/?failure=True')
	dirname = common.getRandomStr(32)
	dirPath = os.path.dirname(os.path.abspath(__file__))+"/tmp/{dirname}".format(dirname=dirname)
	os.makedirs(dirPath)
	filePath = "{path}/{file}".format(path=dirPath, file=tweetsFile.filename)
	tweetsFile.save(filePath)
	dirPath = os.path.abspath(dirPath)
	session['filePath'] = os.path.abspath(filePath)
	try:
		auth = tweepy.OAuthHandler(consumerKey, consumerSecret, 'http://localhost:8080/makebot')
		url = auth.get_authorization_url()
		session['consumerKey'] = consumerKey
		session['consumerSecret'] = consumerSecret
		session['requestToken'] = auth.request_token
	except tweepy.TweepError:
		redirect('/?failure=True')
	redirect(url)

@app.route('/makebot', method='GET')
def makebot():
	session = request.environ.get('beaker.session')
	consumerKey = session.get('consumerKey', None)
	consumerSecret = session.get('consumerSecret', None)
	filePath = session.get('filePath', None)
	if not consumerKey and not consumerSecret:
		redirect('/?failure=True')

	auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
	auth.request_token = session.get('requestToken')
	session.delete()
	auth.get_access_token(request.query.oauth_verifier)

	from app.controllers.makebot import MakeBot
	botMaker = MakeBot(auth)
	botMaker.makeZip(filePath)
	dirname = os.path.basename(botMaker.getDirPath())
	os.system('./delSession.sh')
	os.system('./delBot.sh')
	return template('download', url=dirname)

@app.route('/delete', method='GET')
def deleteFiles():
	url = request.query.url
	os.rmdir(url)

@app.route('/download/<filename:path>', method='GET')
def download(filename):
	name, ext = os.path.splitext(filename)
	root = os.path.dirname(os.path.abspath(__file__))+'/tmp/'+name+'/'
	return static_file(filename, root=root, download='bot.zip')
