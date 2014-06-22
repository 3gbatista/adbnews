from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc.methods import media, posts
from wordpress_xmlrpc.methods import taxonomies
import getPic
import MySQLdb


def postArticle(art,title,im,category,tags):

    host = ""
    user = ""
    password = ""
    conn = MySQLdb.connect(host=host, user = user, passwd = password, db="")
    cursor = conn.cursor()
   
    cursor.execute("UPDATE scraped_articles SET paraphrase_flag = 0 WHERE title = %s",(title))
    data = cursor.fetchall()
    cursor.close()
    conn.close()


    
    client = Client("wp url","admin","")
    # set to the path to your file
    if len(im)<2:
        print im
        im = getPic.searchPic(title)
    else:
        print im
        im = getPic.savePic(im)
    filename = "google_images/"+im
      
      
        
    # prepare metadata
    data = {
            'name': filename,
            'type': "image/jpg",  # mimetype
            }

    # read the binary file and let the XMLRPC library encode it into base64
    with open(filename, 'rb') as img:
        data['bits'] = xmlrpc_client.Binary(img.read())

    response = client.call(media.UploadFile(data))
    # response == {
    #       'id': 6,
    #       'file': 'picture.jpg'
    #       'url': 'http://www.example.com/wp-content/uploads/2012/04/16/picture.jpg',
    #       'type': 'image/jpg',
    # }
    print response
    attachment_id = response['id']


    post = WordPressPost()
    post.title = str(title)

    post.terms_names = {
            'post_tag': ["premium"],
            'category': ['business'],
    }

    post.content = str(art)
    post.post_status = 'publish'
    post.thumbnail = attachment_id
    post.id = client.call(posts.NewPost(post))

    print "uploaded!"
