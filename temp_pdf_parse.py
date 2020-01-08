import requests
import PyPDF2
import slate3k as slate
import warnings
warnings.filterwarnings("ignore", message="Numerical issues were encountered ")
file_url = "https://arxiv.org/ftp/arxiv/papers/1711/1711.11508.pdf"


def parsePdf(file_url):
        # creating a pdf file object
        try:
            r = requests.get(file_url, stream=True)

            with open("temp.pdf", "wb") as pdf:
                for chunk in r.iter_content(chunk_size=1024):

                    # writing one chunk at a time to pdf file
                    if chunk:
                        pdf.write(chunk)

            pdfFileObj = open(
                "temp.pdf", 'rb')

            extracted_text = slate.PDF(pdfFileObj)
        # creating a pdf reader object
            pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

        # printing number of pages in pdf file
            numPage = pdfReader.numPages
        # print(numPage)
        # creating a page object
        # pageObj = pdfReader.getPage(0)

        # extracting text from page
        # text = pageObj.extractText()
        # print(text)
        # print(extracted_text)
        # closing the pdf file object
        except:
            extracted_text = "No text"
            numPage = 0
            # print('Not a PDF')
        pdfFileObj.close()
        return extracted_text, numPage

# text, page = parsePdf(file_url)
# print(s)
