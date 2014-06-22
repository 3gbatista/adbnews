import gethtml
import articletext
import articletrans
import getarticle
import test1
from bs4 import BeautifulSoup
import multihtml

def getTrans(url):
	article_attrs = getarticle.getReadableArticle(url)
	readable = ""
	readable_article = article_attrs[0]
	for u in readable_article:
	    try:
	        readable+= u.encode('UTF-8')
	    except:
	        c=0
	readable_title = article_attrs[1]



	chinese = test1.translateString("en","zh-CN",str(readable))
	english = test1.translateString("zh-CN","en",chinese)

	#print readable_article[100:200]
	#print chinese[100:200]
	#print english[100:200]
	#print english
	return english
