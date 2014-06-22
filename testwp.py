import datetime, xmlrpclib

def postArticle(articleText):
    wp_url = ""
    wp_username = ""
    wp_password = ""
    wp_blogid = ""

    now= str(datetime.datetime.now())
   
    print now
    
    status_draft = 0
    status_published = 1

    server = xmlrpclib.ServerProxy(wp_url)

    title = "Title with spaces"
    content = articleText
    date_created = xmlrpclib.DateTime(now)
    categories = ["entertainment"]
    tags = ["premium"]
    thumbnail = "http://distilleryimage5.s3.amazonaws.com/73c66300257211e28a411231380e7e4a_6.jpg"
    data = {'title': title, 'description': content, 'dateCreated': date_created, 'categories': categories, 'mt_keywords': tags}

    post_id = server.metaWeblog.newPost(wp_blogid, wp_username, wp_password, data, status_published)



postArticle("welcome~!!")
