from bs4 import BeautifulSoup
from requests import get
import sqlite3
from sys import argv


def lista():

    URL = 'http://www.90minut.pl/liga/1/liga11211.html'

    page = get(URL)
    bs = BeautifulSoup(page.content, 'html.parser')

    lista = []
    for clubs in bs.find_all('td', width="180"):
        t = clubs.get_text().strip()
        lista.append(t)

    return lista


# pary = []

# a = 0
# b = 1
# for i in range(34):
#     print(f'Kolejka nr {i+1}')
#     for x in range(8):
#         print(f'{lista[a]} - {lista[b]}')
#         # print(lista[a] + lista[b])
#         a += 2
#         b += 2
