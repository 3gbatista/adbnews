#execfile("webscraper/googlesearch.py")
import urllib 
import mechanize 
from bs4 import BeautifulSoup 
import re

def getGoogleLinks(url):
	url = url.replace(" ","+")
	url = "https://www.google.com/search?q="+url+"&num=100&filter=0"
	results_arr = []
	br = mechanize.Browser()
	br.set_handle_robots(False)
	br.addheaders = [('User-agent', 'Firefox')]

	htmltext = br.open(url).read()
	soup = BeautifulSoup(htmltext)
	searchres =  soup.findAll('div',attrs={"id":"search"})
	searchtext =  str(searchres[0])
	soup1 = BeautifulSoup(searchtext)
	lis = soup1.findAll("li")

	regex = "q(?!.*q).*?&amp"
	pattern = re.compile(regex)
	for li in lis:
		soup3 = BeautifulSoup(str(li))
		links = soup3.findAll('a')
		rep =  links[0]
		results = re.findall(pattern,str(rep))
		if len(results)>0:
			if "http" in str(results[0]):
				results_arr.append(str(results[0].replace("q=htt","htt").replace("&amp",""))) 
		#print links[0]
	return results_arr


