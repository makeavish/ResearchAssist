import re
from pdf_parse import parsePdf
from get_ref_list import findReferenceList
# Python program to convert a list to string

# Function to convert
def listToString(s,ind):
	# initialize an empty string
	str1 = ""

	# traverse in the string
	for j in range(ind,len(s)):
		str1 += s[j]

	# return string
	return str1
def ref(file_url):
    finalReferList = []
    text, page = parsePdf(file_url)
    refAt = -1

    for i in range(page-1,-1,-1):
        eachpage = text[i]
        wordList = eachpage.split()
        for j in range(len(wordList)):
            wordList[j] = wordList[j].lower()
            if(wordList[j] == 'references'or wordList[j] == 'bibliography'):
                refAt = i
                # text = listToString(wordList, j)
                # finalReferList = findReferenceList(text)
                break

    if(refAt!=-1 and refAt!=page-1):
        for i in range(refAt+1,page):
            eachpage = text[i]
            eachpage=eachpage.split(". \n\n")
            finalReferList.append(findReferenceList(eachpage))
    print(finalReferList)
