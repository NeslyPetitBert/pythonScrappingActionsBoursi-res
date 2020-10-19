
# pip install requests BeautifulSoup4 lxml json
import json
import requests
from bs4 import BeautifulSoup

def getContent(page):
    url = link + str(page)
    return requests.get(url).text


def scraping():
    page = 1
    bdd = []
    for page in range(limit_page):
        dataHtml = getContent(page)
        dataParse = BeautifulSoup(dataHtml, "lxml")
        posts = dataParse.findAll("div", {"class": "post"})
        for post in posts:
            element = {}
            title = post.find("h4")
            element["title"] = title.text
            element["url"] = title.findNext("a").attrs["href"]
            element["date"] = post.find("div", {"class": "entry-meta"}).findNext("a").text
            element["text"] = post.find("p").text.split("...")[0]+"..."
            element["id"] = post.attrs["id"]
            bdd.append(element)
    saveData(bdd)
            
def saveData(data):
    with open("scraping.json", "w+", encoding="utf-8") as outfile:
        json.dump(data, outfile)
        

if __name__ == "__main__":
    limit_page = 5
    link = "https://fenetre-sur-cours.com/category/section-intraday-ct/points-intraday/page/"
    #getContent(0)
    scraping()
