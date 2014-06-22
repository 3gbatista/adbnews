import gethtml
import articletext
import articletrans
import getarticle
import test1
from bs4 import BeautifulSoup
import paraphrase
import googlesearch
import articletext

urls = []
topics = []
visited = []
root_topic = "news"

for googl in googlesearch.getGoogleLinks(root_topic):
    urls.append(googl)

for u in urls:
    mytext =  articletext.getArticle(u)
    keywords = articletext.getKeywords(mytext)
    for k in keywords:
        if k not in topics:
            topics.append(k)
    print mytext

#print paraphrase.getTrans("http://sparkbrowser.com")
