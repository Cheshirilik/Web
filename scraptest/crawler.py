from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now())


def get_soup(url):
    try:
        html = urlopen("http://en.wikipedia.org" + url)
    except HTTPError:                                # 404 или похожее
        return None

    return BeautifulSoup(html.read(), "lxml")


def get_wiki_links(url):
    soup = get_soup(url)

    return soup.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))


pages = set()
def get_wiki_links1(url):
    global pages

    soup = get_soup(url)
    for i in soup.findAll("a", href=re.compile("^(/wiki/)")):
        if "href" in i.attrs:
            if i.attrs['href'] not in pages:
                new = i.attrs['href']
                print(new)
                pages.add(new)
                get_wiki_links1(new)


def get_wiki_links2(url):
    global pages

    soup = get_soup(url)
    try:
        print("h1.get_text = " + soup.h1.get_text())
        print("mw-content-text = ")
        print(soup.find(id="mw-content-text").findAll("p")[0])
    except AttributeError:
        print("Something bad happened")

    for i in soup.findAll("a", href=re.compile("^(/wiki/)")):
        if "href" in i.attrs:
            if i.attrs['href'] not in pages:
                new = i.attrs['href']
                print("------\n" + new)
                pages.add(new)
                get_wiki_links2(new)


#======== MAIN ========
# links = get_wiki_links("/wiki/Kevin_Bacon")
# print(links)
# while len(links) > 0:
#     article = links[random.randint(0, len(links)-1)].attrs["href"]
#     print(article)
#     links = get_wiki_links(article)

# get_wiki_links1("")
# get_wiki_links1("/wiki/Kevin_Bacon")

get_wiki_links2("")

