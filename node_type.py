import re

# p=re.compile('.pdf')

# print(p.findall("abcd.txt"))

def isPDF(link):
    p=re.compile('.pdf')
    x=p.findall(link)
    if(x==[]):
        return 0
    else:
        return 1
