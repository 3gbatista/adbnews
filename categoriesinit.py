#execfile("webscraper/categoriesinit.py")
import urllib 
import googlesearch
import mechanize 
from bs4 import BeautifulSoup 
import re


keyword_dict = []
br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Firefox')]

categories = ["business","celebrity","entertainment","trading","online broker","equity trading"]



for cat in categories:
    myfile = open("categorieslist/"+cat.replace(" ","_")+".txt","w+")
    myfile.close()
    myfile = open("categorieslist/"+cat.replace(" ","_")+".txt","a")
    linklist = googlesearch.getGoogleLinks(cat)
    for link in linklist:
        try:
            htmltext = urllib.urlopen(link).read()
            soup = BeautifulSoup(htmltext)
            res = soup.findAll('meta',attrs={"name":"keywords"})
            for r in res:
                keylist =  r['content']
                
                for key in keylist.split(","):
                    myfile.write(str(key)+"\n")
        except:
            print "err"
    myfile.close()            


