import urllib
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

def codechef_web_scraping(username):
	base="https://www.codechef.com/users/"
	profile=base+username
	# print(profile)
	try:
		req = Request(profile, headers={'User-Agent': 'Mozilla/5.0'})
		web_byte = urlopen(req).read()
		webpage = web_byte.decode('utf-8')
		# print(webpage)
		soup=BeautifulSoup(webpage,'lxml')
		deepak=soup.select('.user-details')

		# print(deepak[0].attrs['colour'])
		return 1,deepak[0]
		# deepak=deepak.unicode('utf-8')
		# for i in deepak:
		# print(i)
	except urllib.error.HTTPError as err:
		if err.code == 404:
			print("Page not found!")
			return 0,username+" not found on "+"codechef!"
		elif err.code == 403:
			print("Access denied!")
			return 0,"Access denied!"
		else:
			print("Something happened! Error code", err.code)
			return 0,"Something happened! Error code "
	except urllib.error.URLError as err:
		print("Some other error happened:", err.reason)
		return 0,"Some other error happened:\check your internet connectivity"
