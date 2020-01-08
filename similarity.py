import requests
from bs4 import BeautifulSoup
from nltk.tokenize import RegexpTokenizer
from collections import OrderedDict
import math
import re
from pdf_parse import parsePdf

ob = RegexpTokenizer(r'\w+')

# link1 = "https://pdfs.semanticscholar.org/1c0c/0fa35d4ff8a2f925eb955e48d655494bd167.pdf"
# link2 = "http://cecas.clemson.edu/~stb/ece847/projects/Multiperson_Track_KF.pdf"


def listToString(s):
	# initialize an empty string
	str1 = ""

	# traverse in the string
	for j in range(0, len(s)):
		str1 += s[j]

	# return string
	return str1

def text(link):
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')

    tokenizer = RegexpTokenizer(r'\w+')
    for script in soup(["script", "style"]):
        script.decompose()    # rip it out
    s = soup.get_text().strip()
    # print(s)
    # .encode('utf-8')
    #s='hello there there this is this hello'
    # s1=set()

    s2 = tokenizer.tokenize(s)
    s2.sort()

    return s2


def dict(text):
    dict = {}
    for word in text:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1
    # for word, freq in dict.items():
        # print(word+":"+str(freq))
    return dict


def sumofFreq(d1, d2):
    sum = 0
    for word in d1:
        if word in d2:
            sum = sum+(d1[word]*d2[word])
    return sum


def mag(dic1):
    mag = 0
    for word, value in dic1.items():
        mag = mag+(value*value)
    return mag


def sim(link1, link2):
	
	doc1 = text(link1)
	doc2 = text(link2)
	dic1 = dict(doc1)
	dic2 = dict(doc2)
	fsum = sumofFreq(dic1, dic2)
	mag1 = mag(dic1)
	mag2 = mag(dic2)
	if mag1==0 or mag2==0:
		return 0
	cos = float(fsum/(math.sqrt(mag1)*math.sqrt(mag2)))
	return float(cos)


def simPDF(link1, link2):
	
	doc1, n = parsePdf(link1)
	doc2, n1 = parsePdf(link2)
	# if n1 == 0 or n == 0:
	# 	return 0
	text1 = listToString(doc1)
	text2 = listToString(doc2)
	s1=ob.tokenize(text1)
	s2=ob.tokenize(text2)
	dic1 = dict(s1)
	dic2 = dict(s2)
	# print(dic1)
	# print(dic2)
	fsum = sumofFreq(dic1, dic2)
	# print(fsum)
	mag1 = mag(dic1)
	mag2 = mag(dic2)
	if mag1 == 0 or mag2 == 0:
		# print('lah')
		return 0
	cos = float(fsum/(math.sqrt(mag1)*math.sqrt(mag2)))
	# print(cos)
	return float(cos)


