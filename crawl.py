import requests
import re
from bs4 import BeautifulSoup
from queue import PriorityQueue
from similarity import sim
from get_pdf_list import getPDF

def isPDF(link):
    p = re.compile('.pdf')
    x = p.findall(link)
    if(x == []):
        return 0
    else:
        return 1

def crawlL(seed_url, num_pdf):
    visited = set()
    pdfs = set()
    queue = PriorityQueue()
    queue.put((1, seed_url))

    while queue.qsize() != 0:
        if len(pdfs) >= num_pdf:
            break
        link = queue.get()
        pdfs.update(getPDF(link[1]))

        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0"}
            link[1] = requests.get(link[1]).url
            page = requests.get(link[1])
            page_content = BeautifulSoup(page.content, 'html.parser')
        except:
            try:
                link[1] = "https://" + link[1]
                link[1] = requests.get(link[1]).url
                page = requests.get(link[1])
                page_content = BeautifulSoup(page.content, 'html.parser')
            except:
                # print("Invalid Link")
                continue
        for links in page_content.find_all('a'):
            links = links.get('href')
            if links not in visited:
                try:
                    # link = "https://" + links
                    links = requests.get(links).url
                    xyz = requests.get(links)
                    score = sim(seed_url, links)
                    visited.add(links)
                    queue.put((-score, str(links)))
                except Exception as E:
                    # print(E)
                    continue
    return pdfs


# url = 'http://security.cs.rpi.edu/courses/binexp-spring2015/'
# q =crawlL(url,10)
# print(q)
