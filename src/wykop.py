import urllib
import urllib.request
from bs4 import BeautifulSoup

thepage = urllib.request.urlopen("https://www.wykop.pl/ludzie/wpisy/Xalimer/")
soup = BeautifulSoup(thepage,"html.parser")

print(soup.find('title').text)

i=1

for wpis in soup.findAll("div",{"class":"text"}):
    print(i)
    print(wpis.find('p').text)
    i=i+1