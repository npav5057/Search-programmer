import urllib.request
import simplejson as JSON
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

def codeforces_web_scraping(username):
	base="http://codeforces.com/api/user.info?handles="
	profile=base+username
	try:
		request_url = urllib.request.urlopen(profile)
		request=request_url.read().decode("utf-8")
		data=JSON.loads(request)
		return 1,data['result'][0]
	except urllib.error.HTTPError as err:
		if err.code == 404:
			print("Page not found!")
			return 0,"Page not found!"
		elif err.code == 403:
			print("Access denied!")
			return 0,"Access denied!"
		else:
			print("Something happened! Error code", err.code)
			return 0,username+" not found on "+"codeforces!"
	except urllib.error.URLError as err:
		print("Some other error happened:", err.reason)
		return 0,"Some other error happened:/check your internet connectivity"
