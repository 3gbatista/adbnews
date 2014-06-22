import urllib
import mechanize
url = "http://www.latimes.com/"
br = mechanize.Browser()

htmltext = br.open(url).read()
print htmltext
