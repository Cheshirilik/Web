from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now())

def get_soup(url):
    try:
        html = urlopen("http://wikipedia.org" + url)
    except HTTPError:                                # 404 или похожее
        return None

    return BeautifulSoup(html.read(), "lxml")


def get_wiki_links(url):
    soup = get_soup(url)

    return soup.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))


#======== MAIN ========
links = get_wiki_links("/wiki/Kevin_Bacon")
print(links)
while len(links) > 0:
    article = links[random.randint(0, len(links)-1)].attrs["href"]
    print(article)
    links = get_wiki_links(article)
