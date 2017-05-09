from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


def get_soup(url):
    try:
        html = urlopen(url)

    except HTTPError:                                # 404 или похожее
        return None

    return BeautifulSoup(html.read(), "lxml")


def get_head(url):
    try:
        soup = get_soup(url)
        obj = soup.html.head
    except AttributeError:                           # обращение к атрибуту отсутствующего тэга
        return None
    else:
        return obj


def get_color(url, color):
    try:
        soup = get_soup(url)
    except:                           # обращение к атрибуту отсутствующего тэга
        return None
    else:
        return soup.findAll("span", color)


def test():
    print("Start test\n")

    soup = get_soup("http://pythonscraping.com/pages/page3.html")

    # for i in soup.find("table", {"id": "giftList"}).descendants:
    for i in soup.find("table", {"id": "giftList"}).children:
    # for i in soup.find("table", {"id": "giftList"}).tr.next_siblings:
        print(i)

    print(soup.find("img", {"src": "../img/gifts/img1.jpg"}).parent.previous_sibling)



    print("\nEnd test")


########################
# obj = get_head("http://pythonscraping.com/pages/page1.html")
# if obj:
#     print(obj)
# else:
#     print("Tag not found!")

# name_list = get_color("http://pythonscraping.com/pages/warandpeace.html", {"class": "green"})
# if name_list:
#     for name in name_list:
#         print(name.get_text())
# else:
#     print("Color not found!")

test()


