from typing import List
import requests
from bs4 import BeautifulSoup


urls = []
num = 50


def get_html() -> None:
    for url in urls:
        try:
            response = requests.get(url)
            bs = BeautifulSoup(response.text, 'html.parser')
        except Exception as e:
            print(e)
        else:
            with open('sitedata.txt', 'a', encoding='utf-8') as file:
                file.write(str(bs))
            print('Данные сохранены')


def get_prime(number: int) -> List[int]:
    prime = [True for i in range(number + 1)]
    p = 2
    while p * p <= number:
        if prime[p]:
            for i in range(p * p, number + 1, p):
                prime[i] = False
        p += 1
    for p in range(2, number + 1):
        if prime[p]:
            print(p)


if __name__ == '__main__':
    get_html()
    get_prime(number=num)
