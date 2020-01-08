import requests
import os
import sys
from urllib.parse import urljoin
# url = "http://security.cs.rpi.edu/courses/binexp-spring2015/"

def getPDF(url):
	try:
		from bs4 import BeautifulSoup
	except ImportError:
		print("[*] Please download and install Beautiful Soup first!")
		sys.exit(0)

	pdfs = set()
	headers = {
		"User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0"}
	url = requests.get(url).url
	page = requests.get(url)
	soup = BeautifulSoup(
		page.content, 'html.parser')
	for tag in soup.findAll('a', href=True):
		tag['href'] = urljoin(url, tag['href'])
		if os.path.splitext(os.path.basename(tag['href']))[1] == '.pdf':
			pdfs.add(tag['href'])
	return pdfs
