import urllib
import mechanize
from bs4 import BeautifulSoup
import MySQLdb
import datetime
import testwp


def mySearch(term):
    links = searchAP(term)
    for l in links:
        insertDB(getArticle(l))
        print l
    print "Done..."        



def insertDB(resp):
    host = ""
    user = ""
    password = ""
    conn = MySQLdb.connect(host=host, user = user, passwd = password, db="")
    cursor = conn.cursor()
   
    cursor.execute("INSERT INTO scraped_articles (text,title,date,author,url,picture_url) VALUES (%s,%s,%s,%s,%s,%s)",(resp[0],resp[1],resp[2],resp[3],resp[4],resp[5]))
    data = cursor.fetchall()
    cursor.close()
    conn.close()


    conn = MySQLdb.connect(host=host, user = user, passwd = password, db="")
    cursor = conn.cursor()
    cursor.execute ("UPDATE scraped_articles SET paraphrase_flag = 1 WHERE url = %s",(resp[4]))
    data = cursor.fetchall()
    cursor.close()
    conn.close()






def searchAP(searchterm):
    newlinks = []
    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    browser.addheaders = [('User-agent', 'Firefox')]
    text = ""
    start = 0
    while "There were no matches for your search" not in text:
        url = "http://hosted.ap.org/dynamic/external/search.hosted.ap.org/wireCoreTool/Search?SITE=AP&SECTION=HOME&TEMPLATE=DEFAULT&start_at="+str(start)+"&query="+searchterm
        text = urllib.urlopen(url).read()
        soup = BeautifulSoup(text)

        

        results = soup.findAll('a')
        for r in results:
            if "TEMPLATE=DEFAULT" in r['href'] and "/dynamic" in r["href"]:
                newlinks.append("http://hosted.ap.org"+ str(r["href"]))
        start +=25

    return newlinks


def getArticle(url):
    response = []
    final_text = ""
    text = urllib.urlopen(url).read()
    soup = BeautifulSoup(text)
    results = soup.findAll('p',attrs={"class":"ap-story-p"})
    for r in results:
        final_text += r.text
    response.append(final_text.encode('ascii','ignore'))
    title = ""
    ti = soup.findAll("span",attrs={"class":"headline entry-title"})
    for r in ti:
        title += r.text
    response.append(title)

    timestamp = ""
    ts = soup.findAll("div",attrs={"class":"timestamp updated"})
    for ris in ts:
        timestamp+=ris.text
    response.append(timestamp)

    author = ""
    aut = soup.findAll("span",attrs={"class":"fn"})
    for a in aut:
        author+=a.text
    response.append(author)

    response.append(url)
    

    picture_url = ""
    pic = soup.findAll("img",attrs={"class":"ap-smallphoto-img"})
    for pi in pic:
        picture_url+="http://hosted.ap.org"+pi['src'].replace("small","big")
    response.append(picture_url)

    
    return response        
    



mySearch("trading profit")

