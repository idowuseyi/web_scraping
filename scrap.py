from bs4 import BeautifulSoup
import requests

with open("../Ecom_Website/index.html") as html_file:
    soup = BeautifulSoup(html_file, "lxml")
    
for product in soup.find("section", class_="section-p1").find_all("div", class_="pro"):
    name = product.h5.text
    print(name)

    img_link = product.img["src"]
    print(img_link)

    price = product.h4.text
    print(price)
    
    print()