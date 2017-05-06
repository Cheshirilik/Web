from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


def get_tag(url, tag=None):
    try:
        html = urlopen(url)

    except HTTPError:                                # 404 или похожее
        return None

    try:
        soup = BeautifulSoup(html.read())
        obj = soup.html.head
    except AttributeError:                           # обращение к атрибуту отсутствующего тэга
        return None
    else:
        if obj:
            return obj
        else:                                        # не найден тэг
            return None


obj = get_tag("http://pythonscraping.com/pages/page1.html")
if obj:
    print(obj)
else:  # не найден тэг
    print("Tag not found!")



