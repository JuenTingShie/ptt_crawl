import requests
import os
from bs4 import BeautifulSoup


def get_list(url):

    def get_soup(request):
        soup = BeautifulSoup(request.content, 'lxml')
        items = soup.find_all('div', {'class': 'title'})
        return items

    r = requests.Session()  #取得一次Cookie
    request = r.get(url)  #第一次GET
    if request.history:  #如果有歷史紀錄代表有轉址過
        request = r.post(  #對最後一個網址做POST
            request.url,
            data={
                'from': request.url,
                'yes': 'yes',
            })
        request = r.get(url)  #再對原始網址做GET
    print(get_soup(request))


if __name__ == "__main__":
    c = get_list("https://www.ptt.cc/bbs/Gossiping/index.html")
    print(c)
# items_list = []
# for item in items:
#     title = item.find('a').text
#     url = item.find('a').get('href')
#     a = ClassItem(title, ROOT_URL+url)
#     items_list.append(a)
#     print(items_list.index(a), a.name)

# num = input('請輸入要瀏覽的文章(exit退出): \n')
# if(num == 'exit'):
#     pass
# else:
#     num = int(num)
#     item_request = requests.get(a.url)
#     if(item_request.status_code == requests.codes.ok):
#         soup = BeautifulSoup(item_request.content, 'lxml')
#         item_c = soup.find('div', {'id': 'main-container'})
#         a.content(item_c.text)
#         print(a.content)

# class Board:
#     def __init__(self, board_href, board_name, board_class, board_title):
#         self.href = href
#         self.board_name = board_name
#         self.board_class = board_class
#         self.board_title = board_title
