from bs4 import BeautifulSoup
from requests import get
import sqlite3
from sys import argv


def zestaw_par():
    URL = 'http://www.90minut.pl/liga/1/liga11211.html'

    page = get(URL)
    bs = BeautifulSoup(page.content, 'html.parser')

    lista = []
    for clubs in bs.find_all('td', width="180"):
        t = clubs.get_text().strip()
        lista.append(t)

    a = 0
    b = 16
    zestaw_par = []
    for i in range(34):
        zestaw_par.append(lista[a:b])
        a += 16
        b += 16

    return zestaw_par
