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
	if not request.forms.get('consumerKey') or not request.forms.get('consumerSecret') or not request.files.get('tweetsFile'):
		error(session)
		redirect('/?failure=True')
	consumerKey = request.forms.get('consumerKey')
	consumerSecret = request.forms.get('consumerSecret')
	tweetsFile = request.files.get('tweetsFile')
	
	# Checking extention
	name, ext = os.path.splitext(tweetsFile.filename)
	if not ext =='.txt':
		error(session)
		redirect('/?failure=True')
	
	# Create session directory
	dirname = common.getRandomStr(32)
	dirPath = os.path.dirname(os.path.abspath(__file__))+"/tmp/{dirname}".format(dirname=dirname)
	os.makedirs(dirPath)
	filePath = "{path}/{file}".format(path=dirPath, file=tweetsFile.filename)
	tweetsFile.save(filePath)
	dirPath = os.path.abspath(dirPath)
	session['filePath'] = os.path.abspath(filePath)
	try:
		auth = tweepy.OAuthHandler(consumerKey, consumerSecret, 'https://botmaker.herokuapp.com/makebot')
		url = auth.get_authorization_url()
		session['consumerKey'] = consumerKey
		session['consumerSecret'] = consumerSecret
		session['requestToken'] = auth.request_token
	except tweepy.TweepError:
		error(session)
		redirect('/?failure=True')
	redirect(url)

@app.route('/makebot', method='GET')
def makebot():
	session = request.environ.get('beaker.session')
	consumerKey = session.get('consumerKey', None)
	consumerSecret = session.get('consumerSecret', None)
	filePath = session.get('filePath', None)
	if not consumerKey and not consumerSecret:
		error(session)
		redirect('/?failure=True')

	auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
	auth.request_token = session.get('requestToken')
	try:
		auth.get_access_token(request.query.oauth_verifier)
	except tweepy.TweepError:
		error(session)
		redirect('/?failure=True')

	# Create zip file
	from app.controllers.makebot import MakeBot
	botMaker = MakeBot(auth)
	botMaker.makeZip(filePath)
	dirname = os.path.basename(botMaker.getDirPath())
	return template('download', url=dirname)


@app.route('/download/<filename:path>', method='GET')
def download(filename):
	session = request.environ.get('beaker.session')
	
	# Checking user
	name, ext = os.path.splitext(filename)
	if name != os.path.basename(os.path.dirname(session.get('filePath', None))):
		error(session)
		redirect('/?failure=True')
	root = os.path.dirname(os.path.abspath(__file__))+'/tmp/'+name+'/'
	error(session)
	return static_file(filename, root=root, download='bot.zip')

def error(session):
	session.delete()
	os.system('./delSession.sh')
	os.system('./delBot.sh')
	
