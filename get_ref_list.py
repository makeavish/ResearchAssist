from search import find
# data="hi there\nI ma piyush\nhi"

def findReferenceList(data):
    ans=[]
    for lines in data:
        try:
            ans.append(find(lines,1)[0])
        except:
            continue
    return ans

# j=findReferenceList(data)
# print(j)