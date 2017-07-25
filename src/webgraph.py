import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup

myurl = "https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card"

uClient = urlopen(myurl)
page = uClient.read()
uClient.close()
page_soup = BeautifulSoup(page,"html.parser")

print(page_soup.h1.text)

containers = page_soup.findAll("div",{"class":"item-container"})

headers = "brand, product_name, shipping"
file = open("karty.ods","w")
file.write(headers)

for container in containers:
    try:
        brand = container.div.div.a.img["title"]
    except AttributeError:
        brand = "none"

    title_container = container.findAll("a",{"class":"item-title"})
    product_name = title_container[0].text #może[0]?

    shippingg_container = container.findAll("li",{"class":"price-current"})
    shipping = shippingg_container[0].strong.text

    file.write(brand + "," + product_name.replace(",","|") + "," + shipping + "\n")
file.close()