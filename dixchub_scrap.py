from bs4 import BeautifulSoup
import requests
import csv

source = requests.get("https://dixcoverhub.com/").text

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