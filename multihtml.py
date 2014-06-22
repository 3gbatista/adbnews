import urllib
import re
import time
from threading import Thread
import MySQLdb
import mechanize
import readability
from bs4 import BeautifulSoup
from readability.readability import Document
import urlparse
import getarticle


class MultiScrape:
    visited = []
    urls = []
    articletexts = []
    external_links = []
    depth = 0
    counter = 0
    threadlist = []
    root = ""

    def __init__(self, url, depth):
       self.urls.append(url)
       self.visited.append(url)
       self.depth = depth
       self.root = url

   
    def run(self):
        while  len(self.urls)>0:     
            for r in self.urls:
                try: 
                    t = Thread(target=self.scrapeStep, args=(r,))
                    self.threadlist.append(t)
                    t.start()            
                except:
                    nnn = True 
            self.urls = []                
            for g in self.threadlist:
                g.join() 
            self.counter+=1

        return self.articletexts  

    def scrapeStep(self,root):
        br = mechanize.Browser()
        br.set_handle_robots(False)
        br.addheaders = [('User-agent', 'Firefox')]
        print root
        try:     
            html1 = br.open(root).read() 
            try:
                art_text = getarticle.getReadableArticle(root)
                print art_text
                if len(art_text) > 0:
                    myfile = open("categorieslist.txt","a")
                    try:
                        art_text = art_text.decode('UTF-8')
                        if len(art_text) > 500:   
                            myfile.write(art_text+"\n")
                    except:
                        a = 0
                    myfile.close()    
            except:
                s = 0
            for link in br.links():
                newurl =  urlparse.urljoin(link.base_url,link.url)
                if self.root in newurl.replace("www.","") and newurl not in self.visited:
                    self.urls.append(newurl) 
                    self.visited.append(newurl)
                    print newurl
        except:
            f = 0               





def getReadableArticle(url):
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.addheaders = [('User-agent', 'Firefox')]

    html = br.open(url).read()

    readable_article = Document(html).summary()
    readable_title = Document(html).short_title()

    soup = BeautifulSoup(readable_article)

    final_article = soup.text

    links = soup.findAll('img', src=True)

    title_article = []
    title_article.append(final_article)
    title_article.append(readable_title)
    return title_article

    



def dungalo(urls):
    article_text =getReadableArticle(urls)[0]
    d[urls] = article_text

        

def getMultiHtml(urlsList,steps):

    for urls1 in urlsList:
        try:
            t = Thread(target=scraper, args=(urls1,steps,))
            threadlist.append(t)
            t.start()            
        except:
            nnn = True

    for g in threadlist:
        g.join()


url1 = "http://sparkbrowser.com"
myfile = open("categorieslist.txt","w+")
myfile.close()
mysite = MultiScrape(url1,3)
myarray =  mysite.run()


