
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
    #data = "client=t&text=2)%09Theology%20should%20not%20be%20questioned%20with%20philosophical%20reasoning%20because%20it%20deals%20with%20questions%20that%20are%20unexplainable%2C%20so%20trying%20to%20prove%20or%20disprove%20them%20with%20reason%20is%20incorrect.%20Religious%20beliefs%20are%20in%20essence%20an%20absence%20of%20reason%20and%20just%20accepting%20things%20on%20faith.%20It%20seems%20to%20defeat%20the%20purpose%20of%20religion%20to%20change%20views%20after%20questioning%20a%20belief%20because%20then%20the%20belief%20is%20not%20taken%20on%20faith%2C%20but%20upon%20empirical%20evidence.%20If%20there%20is%20an%20absence%20of%20faith%20in%20a%20belief%20it%20is%20no%20longer%20a%20religious%20belief%20and%20it%20is%20just%20a%20fact%3B%20therefore%20it%20is%20equally%20reasonable%20to%20not%20question%20religious%20beliefs%20and%20take%20them%20on%20faith.%202)%09Theology%20should%20not%20be%20questioned%20with%20philosophical%20reasoning%20because%20it%20deals%20with%20questions%20that%20are%20unexplainable%2C%20so%20trying%20to%20prove%20or%20disprove%20them%20with%20reason%20is%20incorrect.%20Religious%20beliefs%20are%20in%20essence%20an%20absence%20of%20reason%20and%20just%20accepting%20things%20on%20faith.%20It%20seems%20to%20defeat%20the%20purpose%20of%20religion%20to%20change%20views%20after%20questioning%20a%20belief%20because%20then%20the%20belief%20is%20not%20taken%20on%20faith%2C%20but%20upon%20empirical%20evidence.%20If%20there%20is%20an%20absence%20of%20faith%20in%20a%20belief%20it%20is%20no%20longer%20a%20religious%20belief%20and%20it%20is%20just%20a%20fact%3B%20therefore%20it%20is%20equally%20reasonable%20to%20not%20question%20religious%20beliefs%20and%20take%20them%20on%20faith.%202)%09Theology%20should%20not%20be%20questioned%20with%20philosophical%20reasoning%20because%20it%20deals%20with%20questions%20that%20are%20unexplainable%2C%20so%20trying%20to%20prove%20or%20disprove%20them%20with%20reason%20is%20incorrect.%20Religious%20beliefs%20are%20in%20essence%20an%20absence%20of%20reason%20and%20just%20accepting%20things%20on%20faith.%20It%20seems%20to%20defeat%20the%20purpose%20of%20religion%20to%20change%20views%20after%20questioning%20a%20belief%20because%20then%20the%20belief%20is%20not%20taken%20on%20faith%2C%20but%20upon%20empirical%20evidence.%20If%20there%20is%20an%20absence%20of%20faith%20in%20a%20belief%20it%20is%20no%20longer%20a%20religious%20belief%20and%20it%20is%20just%20a%20fact%3B%20therefore%20it%20is%20equally%20reasonable%20to%20not%20question%20religious%20beliefs%20and%20take%20them%20on%20faith.%202)%09Theology%20should%20not%20be%20questioned%20with%20philosophical%20reasoning%20because%20it%20deals%20with%20questions%20that%20are%20unexplainable%2C%20so%20trying%20to%20prove%20or%20disprove%20them%20with%20reason%20is%20incorrect.%20Religious%20beliefs%20are%20in%20essence%20an%20absence%20of%20reason%20and%20just%20accepting%20things%20on%20faith.%20It%20seems%20to%20defeat%20the%20purpose%20of%20religion%20to%20change%20views%20after%20questioning%20a%20belief%20because%20then%20the%20belief%20is%20not%20taken%20on%20faith%2C%20but%20upon%20empirical%20evidence.%20If%20there%20is%20an%20absence%20of%20faith%20in%20a%20belief%20it%20is%20no%20longer%20a%20religious%20belief%20and%20it%20is%20just%20a%20fact%3B%20therefore%20it%20is%20equally%20reasonable%20to%20not%20question%20religious%20beliefs%20and%20take%20them%20on%20faith.&hl=en&sl=en&tl=ru&ie=UTF-8&oe=UTF-8&multires=1&otf=2&pc=1&ssel=0&tsel=0"
    #Submit the form (POST request). You get the post_url and the request type(POST/GET) the same way with the parameters.
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