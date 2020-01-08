from queue import PriorityQueue
from create_query import query
from crawl import crawlL
from similarity import sim
from similarity import simPDF
from references import ref

def run():
    pdfs = set()
    print('Hello, this is Coco, your research assistant')
    file = input('Please enter url of the pdf\n')
    # print('Here are the references :\n')
    # ref(file)
    # try:
    results = query(file)
    for link in results:
        pdfs.update(crawlL(link,40))
    print(len(pdfs))
    qPDF = PriorityQueue()
    for pdf in pdfs:
        score = simPDF(file, pdf)
        qPDF.put((-score, str(pdf)))
    for i in range(0,min(qPDF.qsize(),10)):
            next_item = qPDF.get()
            print(next_item)
    # except Exception as E:
    #     print(E)

run()
