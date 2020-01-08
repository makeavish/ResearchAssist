# pip install google
try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 
from node_type import isPDF
# to search 
# query = "Geeksforgeeks"
  
def find(query,n):
    ans=[]
    anss=[]
    query+=" research"
    for j in search(query, tld="com", num=2*n,stop=2*n, pause=4): 
        ans.append(j)
    i=0
    while len(anss)!=n and i<len(ans):
        if not isPDF(ans[i]):
            anss.append(ans[i])
        i+=1
    return anss

# j=find("particle physics",10)
# print(j)
