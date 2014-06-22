
from bs4 import BeautifulSoup 
import re
import urllib
import urlparse
import mechanize
import json
import gzip

def translateString(homeLanguage,targetLanguage,transText):  
    post_url = "http://translate.google.com/translate_a/t"
    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    browser.addheaders = [('User-agent', 'Firefox')]

    #These are the parameters you've got from checking with the aforementioned tools
    parameters = {'client' : 't',
                  'text' : transText,
                  'hl' : homeLanguage,
                  'sl' : homeLanguage,
                  'tl' : targetLanguage,
                  'ie' : 'UTF-8',
                  'oe' : 'UTF-8',
                  'multires' : '1',
                  'otf' : '2',
                  'pc' : '0',
                  'ssel' : '0',
                  'tsel' : '0',
                  'sc': '1'
                 }
    #Encode the parameters
    data = urllib.urlencode(parameters)
    
    
    trans_array = browser.open(post_url,data).read().decode('UTF-8')




    #Submit the form (GET request)
    #trans_array =  browser.open(post_url + '?'+ data).read().split('"')
    trans_string = ""
    sections = trans_array.split("]]")
    secarray =sections[0].replace("[[[","").replace("],[","").replace('""',"").split('"')

    co = -1
    for thing in secarray:
        if co %6 ==0:
            trans_string += thing
        co+=1

    return trans_array

    

print translateString("en","es","I am so cool and awesome, you should all build a new house.")
