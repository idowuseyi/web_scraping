# WEB SCRAPING WITH PYTHON BEAUTIFUL SOUP

### INSTALATION
pip install beautifulsoup4, lxml or html5lib, requests

once installed.
It is advantageous to have a glimpse understanding of how html file is structured and how a webpage works.

with open("../Ecom_Website/index.html") as html_file:
    soup = BeautifulSoup(html_file, "lxml")
    
# print(soup.prettify())  # Gives us good indentation of the html file
match = soup.title.text # To get the page title. We can do .title.tex to get the title alone
print(match)

The above will only give us the first match i.e the first title but what if it's not the first title we want.

We can use the find method by passing in some arguments.

We can use the find to narrow down as much as possible

#match = soup.find("section", id="product1")
#match = soup.find("section", class_="section-p1")
product = soup.find("section", class_="section-p1").find("div", class_="des").h5.text
#print(soup.prettify())
print(product)

We can find our data one by one 
product = soup.find("section", class_="section-p1").find("div", class_="pro")

#product_image_link = soup.find("section", class_="section-p1").find("div", class_="des").h5.text

name = product.h5.text
print(name)

img_link = product.img["src"]
print(img_link)

price = product.h4.text
print(price)

Having found the specific repeated information we want, we can use the method find_all which will get all elements specified and loop through it grabbing our specified data

for product in soup.find("section", class_="section-p1").find_all("div", class_="pro"):
    name = product.h5.text
    print(name)

    img_link = product.img["src"]
    print(img_link)

    price = product.h4.text
    print(price)
    
    print()


Let's get the data from an actual website. We will be using dixcoverhub

from bs4 import BeautifulSoup
import requests

source = requests.get("https://dixcoverhub.com/").text

soup = BeautifulSoup(source, "lxml")

# print(soup.prettify())

post = soup.find("article", class_="type-post")
# print(post.prettify())

title = post.a.text
print("Title: ", title)

summary = post.p.text
print("Brief: ", summary)

link = post.a["href"]
print("url: ", link)

datePublished = post.find("span", class_="published").text
print("Published on: ", datePublished)

Final script taking into account unavailable data or information.

from bs4 import BeautifulSoup
import requests
import csv

source = requests.get("url").text

soup = BeautifulSoup(source, "lxml")

csv_file = open("cms_scrape.csv", "w")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Post Title", "Summary", "Learn More", "Application Link", "Date Published"])

for post in soup.find_all("article", class_="type-post"):
    title = post.a.text
    print("Title: ", title)

    summary = post.p.text
    print("Brief: ", summary)

    link = post.a["href"]
    print("url: ", link)
    
    try:    
        source2 = requests.get(link).text
        soup2 = BeautifulSoup(source2, "lxml")
        appLink = soup2.find("div", class_="entry-content").a["href"]
    except Exception as e:
        appLink = None

    print("Application link: ", appLink)
    
    datePublished = post.find("span", class_="published").text
    print("Published on: ", datePublished)
    print()
    
    csv_writer.writerow([title, summary, link, appLink, datePublished])
    
csv_file.close()