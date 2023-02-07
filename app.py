from flask import Flask, render_template, request, flash, redirect
from flask import send_file, url_for, after_this_request
from flask_session import Session
import requests
import sqlite3 as sql
import connection as cn
import codechef,codeforces
import simplejson as JSON
# from config import Config
import os
# import urllib
from dotenv import load_dotenv
# from songs import oauth, ext_down
# from anime import anime_download

load_dotenv()

DATABASE = cn.DATABASE
cn.get_db()

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__),"templates")
STATIC_DIR = os.path.join(os.path.dirname(__file__),"static")

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)
# app.config.from_object(Config)
# session = Session()
# session.init_app(app)


@app.route('/', methods=['POST', 'GET'])
def index():
	return render_template('index.html')

@app.route('/redirecting',methods=['POST','GET'])
def different_platform():
   platform_name=request.form['platform']
   username = request.form['username']
   return redirect(url_for('different_platform_name',username=username,pname=platform_name))

@app.route('/<username>/<pname>',methods=['POST','GET'])
def different_platform_name(username,pname):

   if (pname=="codechef"):
	   check1,massage=codechef.codechef_web_scraping(username)
	   if check1==1:
		   return render_template('index.html',msg1=massage)
	   else:
		   return render_template('index.html',unf=massage)
   else:
	   if (pname=="codeforces"):
		   check2,massage=codeforces.codeforces_web_scraping(username)
		   if check2==1:
			   return render_template('index.html',key1="rating",breaker=":",val1=massage['rating'],key2="organization",val2=massage['organization'],key3="rank",val3=massage['rank'],key4="handle",val4=massage['handle'],key5="friendOfCount",val5=massage['friendOfCount'])
		   else:
			   return render_template('index.html',unf=massage)




if __name__ == '__main__':
   app.run(debug = True)
