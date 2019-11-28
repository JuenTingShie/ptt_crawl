import requests
import os
from bs4 import BeautifulSoup

import defines
from deurl import url_to_code
from show_post import get_list


def refresh_boards():
    request = requests.get('https://www.ptt.cc/bbs/hotboards.html')
    soup = BeautifulSoup(request.content, 'lxml')
    # f = open('boards.txt', 'w', encoding='utf-8')
    c = soup.find_all('a', {'class': 'board'})
    boards = []
    for board in c:
        board_href = board.get('href')
        board_name = board.find('div', {'class': 'board-name'}).text
        board_class = board.find('div', {'class': 'board-class'}).text
        board_title = board.find('div', {'class': 'board-title'}).text
        boards.append([board_name, board_href, board_class, board_title])
    return boards


def show_boards():
    boards = refresh_boards()
    i = 0
    while i < len(boards):
        print(i, end='\t')
        for c in boards[i]:
            if (boards[i].index(c) == 1):
                continue
            else:
                print(c.ljust(10, ' '), end='\t')
        print("")
        if (i % 10 == 9 and i >= 9):
            inp = input('請輸入要觀看的看板: ' +
                        'N(下一頁)U(上一頁)'.rjust(os.get_terminal_size().columns))
            try:
                inp = int(inp)
                get_list(defines.ROOT_URL + boards[inp][1])
                if i <= 9:
                    i = -1
                else:
                    i = i - 10
            except:
                i = boards_switch(inp, i)
        i += 1


def boards_switch(inp, i):

    def next_page(i):
        return i

    def last_page(i):
        if i <= 9:
            return -1
        else:
            return i - 20

    method = {
        'n': next_page(i),
        'N': next_page(i),
        'u': last_page(i),
        'U': last_page(i),
    }

    if (method.get(inp) != None):
        os.system('cls')
        return method.get(inp)
    else:
        os.system('cls')
        print('請出入正確的參數!')
        input('Enter以繼續...')
        os.system('cls')
        if i <= 9:
            return -1
        else:
            return i - 10


def main():
    while (True):
        show_boards()
    # os.system('cls')


if __name__ == "__main__":
    main()
