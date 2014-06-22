import urllib
import mechanize
from bs4 import BeautifulSoup
from urlparse import urlparse
import hashlib

def searchPic(term):
    rettext = ""
    ur = getPic(term)
    if ur != "error":
        rettext = savePic(ur)
    print "searched pic"        
    return rettext        




def getPic(search):
    try:
        browser = mechanize.Browser()
        browser.set_handle_robots(False)
        browser.addheaders = [('User-agent', 'Firefox')]

        htmltext = browser.open("https://www.google.com/search?safe=off&hl=en&biw=1366&bih=178&site=imghp&tbm=isch&sa=1&q="+search.replace(" ","+")).read()
       
        img_urls = []
        soup = BeautifulSoup(htmltext)
        results = soup.findAll("a")
        for r in results:
            try:
                if "imgres?imgurl" in r['href']:
                    img_urls.append( r['href'])
            except:
                a =0
        #print img_urls[0]
        textd = urlparse(str(img_urls[0]))
        return textd.query.split("&")[0].replace("imgurl=","")
        print "got image url"
    except:
        return "error"
        print "error"


def savePic(url):
    uri = ""
    hs = hashlib.sha224(url).hexdigest()
    if ".jpg" in url.lower():
        uri = hs+".jpg"
    if ".png" in url.lower():
        uri = hs+".png"
    if ".gif" in url.lower():
        uri = hs+".gif"
    if ".jpeg" in url:
        uri = hs+".jpeg"        
    print uri
    urllib.urlretrieve(url, "google_images/"+uri)
    return uri
    print "saved pic"
                
#print getPic("dodd frank act")
#searchPic("t3 trading")
