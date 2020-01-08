# import urllib.parse
import requests
import os
import sys
from urllib.parse import urljoin

url = "http://security.cs.rpi.edu/courses/binexp-spring2015/"
def getPDF(url):
	try:
		from bs4 import BeautifulSoup
	except ImportError:
		print("[*] Please download and install Beautiful Soup first!")
		sys.exit(0)

	# download_path = "/Volumes/GoogleDrive/My Drive/College/5th Sem/IR/Lab/IR_Project/test"
	pdfs = set()
	# try:
	#to make it look legit for the url
	headers = {
		"User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0"}

	# i = 0

	page = requests.get(url)
	soup = BeautifulSoup(
		page.content, 'html.parser')  # to parse the website

	# find <a> tags with href in it so you know it is for urls
	for tag in soup.findAll('a', href=True):
		#so that if it doesn't contain the full url it can the url itself to it for the download
		tag['href'] = urljoin(url, tag['href'])

		#this is pretty easy we are getting the extension (splitext) from the last name of the full url(basename)
		#the spiltext splits it into the filename and the extension so the [1] is for the second part(the extension)
		if os.path.splitext(os.path.basename(tag['href']))[1] == '.pdf':
			# current = requests.get(tag['href'])
			# print ("\n[*] Downloading: %s" % (os.path.basename(tag['href'])))
			pdfs.add(tag['href'])
			# open(download_path + "/" + os.path.basename(tag['href']), 'wb').write(current.content)
			# i += 1

		# print ("\n[*] Downloaded %d files" % (i+1))
		# input("[+] Press any key to exit...")

	# except KeyboardInterrupt:
	# 	print ("[*] Exiting...")
	# 	sys.exit(1)

