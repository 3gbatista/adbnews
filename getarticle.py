import nltk
import urllib
import urlparse
from bs4 import BeautifulSoup
from readability.readability import Document
from readability.readability import Document
import mechanize
import datetime
import apnews


br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Firefox')]

def getReadableArticle(url):
        now = datetime.datetime.now()
        resp = ["","","","","",""]
        images = []
        html = br.open(url).read()

        readable_article = Document(html).summary()
        #print readable_article
        #print readable_article
        readable_title = Document(html).title()
        #print readable_title
        soup = BeautifulSoup(readable_article)
        final_article = soup.text
        #print final_article
        #print final_article
        links = soup.findAll('img', src=True)
        for lin in links:
                li = urlparse.urljoin(url,lin['src'])
                print li
                images.append( li)
                
        resp[0] = str(final_article.encode("ascii","ignore"))
        #print resp[0]
        resp[1] = str(readable_title)
        resp[2] = str(now.month)+" "+str(now.day)+" "+str(now.year)+"-"+str(now.hour)+":"+str(now.minute)+":"+str(now.second)
        resp[3] = url
        resp[4] = url
        if len(images)>0:
                resp[5] = images[0]
        else:
                resp[5] = ""
        apnews.insertDB(resp)
        print "inserted resp"
                 
        
        title_article = []
        title_article.append(final_article)
        title_article.append(readable_title)
        title_article.append(images)                
        return title_article

	
#getReadableArticle("http://sparkbrowser.com")
