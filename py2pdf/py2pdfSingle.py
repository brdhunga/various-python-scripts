# import modules
import os
import urllib2
from bs4 import BeautifulSoup
from xhtml2pdf import pisa 
from os.path import expanduser

home = expanduser("~")


# define path and url
path2save = os.path.join(home, 'Documents', 'ebookTDD' )
rootUrl = "http://chimera.labs.oreilly.com/books/1234000000754/"
indexPage = "http://chimera.labs.oreilly.com/books/1234000000754/index.html"
indexPageHtml = (urllib2.urlopen(indexPage)).read()

# make an array of all href in the given url after parsing with beautiful soup
soup = BeautifulSoup(indexPageHtml)
all_spans = soup(attrs={'class': 'chapter'}) # use this list on the main module



# define function to convert html to pdf
def convertHtmlToPdf(sourceHtml, outputFilename):
    # open output file for writing (truncated binary)
    resultFile = open(outputFilename, "w+b")

    # convert HTML to PDF
    pisaStatus = pisa.CreatePDF(
            sourceHtml,                # the HTML to convert
            dest=resultFile)           # file handle to recieve result

    # close output file
    resultFile.close()                 # close output file

    # return True on success and False on errors
    return pisaStatus.err




# Main module
singleHtml = ""

if __name__=="__main__":
    pisa.showLogging()
    for link in all_spans:

        #turns out, href is relative so add rooturl
        pageUrl = rootUrl + (link.a).get('href')
        print pageUrl
        pagehtml = (urllib2.urlopen(pageUrl)).read()
        singleHtml += pagehtml

    outputFilename = os.path.join(path2save, 'singleHtml.pdf')
    convertHtmlToPdf(singleHtml, outputFilename)


    
    
