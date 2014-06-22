import MySQLdb
import datetime
#import testwp
import uploadimage
import hashlib

host = "myhost"
user = "myusername"
password = "mypass"

conn = MySQLdb.connect(host=host, user = user, passwd = password, db="passwrdd")
cursor = conn.cursor()
cursor.execute ("select * from scraped_articles where paraphrase_flag = 1")
data = cursor.fetchall()
for d in data:
    image = d[4]
    category = ["business"]
    tags = ["cars","dogs"]
    art = d[10]
    title = d[13]
    print image
    art =  str(d[1])
    #testwp.postArticle
    uploadimage.postArticle(art,title,image,category,tags)
cursor.close()
conn.close()



