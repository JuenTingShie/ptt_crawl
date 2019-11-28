import requests
from bs4 import BeautifulSoup


def main():
    f = open('2.html', 'w', encoding='utf-8')
    url = "https://imgur.com/t/aww"

    list_request = requests.request(
        'GET', url)
    if(list_request.status_code == requests.codes.ok):
        soup = BeautifulSoup(list_request.content, 'lxml')
        f.write(soup.prettify())
        f.close()


if __name__ == "__main__":
    main()
