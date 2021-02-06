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


def term():
    URL = 'http://www.90minut.pl/liga/1/liga11211.html'
    page = get(URL)
    bs = BeautifulSoup(page.content, 'html.parser')

    lista2 = []  # multiple terms
    for daty in bs.find_all('td', width="190"):
        f = daty.get_text().strip()
        lista2.append(f)

    a = 0
    b = 8
    term = []
    for i in range(34):
        term.append(lista2[a:b])
        a += 8
        b += 8

    return term


def wyniki():
    URL = 'http://www.90minut.pl/liga/1/liga11211.html'
    page = get(URL)
    bs = BeautifulSoup(page.content, 'html.parser')

    lista3 = []  # multiple wyniki
    for wynik in bs.find_all('td', width='50'):
        w = wynik.get_text().strip()
        lista3.append(w)

    a = 0
    b = 8
    wyniki = []  # rezultaty dla poszczególnych kolejek
    for i in range(34):
        wyniki.append(lista3[a:b])
        a += 8
        b += 8

    return wyniki

def date():
    URL = 'http://www.90minut.pl/liga/1/liga11211.html'
    page = get(URL)
    bs = BeautifulSoup(page.content, 'html.parser')

    dates = []  # multiple wyniki
    for wynik in bs.find_all('td', colspan='3'):
        d = wynik.get_text().strip()
        if d != '(wo)':
            dates.append(d)

    return dates