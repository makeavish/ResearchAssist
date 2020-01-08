results = query(file)
    for link in results:
        pdfs.update(crawlL(link,20))
        # print('One More Link Done')
    qPDF = PriorityQueue()
    for pdf in pdfs:
        score = simPDF(file, pdf)
        qPDF.put((-score, str(pdf)))
    for i in range(0,min(qPDF.qsize(),10)):
            next_item = qPDF.get()
            print(next_item)