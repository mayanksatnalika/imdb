import mechanize
from bs4 import BeautifulSoup 
import urllib2
# Create a Browser
b = mechanize.Browser()

# Disable loading robots.txt
b.set_handle_robots(False)

b.addheaders = [('User-agent',
                 'Mozilla/4.0 (compatible; MSIE 5.0; Windows 98;)')]

b.open('http://www.trainman.in/')

# Choose a form
b.select_form(nr=1)


b['pnr'] = '4528466606'

fd = b.submit()

soup = BeautifulSoup(fd.read(),'html5lib')

print(soup)
