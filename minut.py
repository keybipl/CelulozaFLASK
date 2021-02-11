from bs4 import BeautifulSoup
from requests import get
import sqlite3
from sys import argv


def zestaw_par():  # zestaw par dla poszczególnych kolejek
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


def term():  # Terminy spotkań dla poszczególnych kolejek
    URL = 'http://www.90minut.pl/liga/1/liga11211.html'
    page = get(URL)
    bs = BeautifulSoup(page.content, 'html.parser')

    lista2 = []
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

    dates = []
    for wynik in bs.find_all('td', colspan='3'):
        d = wynik.get_text().strip()
        if d != '(wo)':
            dates.append(d)

    return dates


def pause():
    URL = 'http://www.90minut.pl/liga/1/liga11211.html'
    page = get(URL)
    bs = BeautifulSoup(page.content, 'html.parser')

    pause = []
    for wynik in bs.find_all('td', colspan='4'):
        p = wynik.get_text().strip()
        if p[0:6] == 'Pauza:':
            pause.append(p)

    return pause


def club():
    URL = 'http://www.90minut.pl/liga/1/liga11211.html'
    page = get(URL)
    bs = BeautifulSoup(page.content, 'html.parser')

    clubs = []
    for wynik in bs.find_all('td', align='left'):
        for c in wynik.find_all('a', class_='main'):
            d = c.get_text().strip()
            clubs.append(d)

    return clubs


def games():
    URL = 'http://www.90minut.pl/liga/1/liga11211.html'
    page = get(URL)
    bs = BeautifulSoup(page.content, 'html.parser')

    game = []
    for wynik in bs.find_all('td', align='left'):
        for c in wynik.find_all('a', class_='main'):
            p = c.find_next('td').get_text().strip()
            game.append(p)

    return game


def points():
    URL = 'http://www.90minut.pl/liga/1/liga11211.html'
    page = get(URL)
    bs = BeautifulSoup(page.content, 'html.parser')

    point = []
    for wynik in bs.find_all('td', align='left'):
        for c in wynik.find_all('a', class_='main'):
            p = c.find_next('td').find_next('td').get_text().strip()
            point.append(p)

    return point


def goals():
    URL = 'http://www.90minut.pl/liga/1/liga11211.html'
    page = get(URL)
    bs = BeautifulSoup(page.content, 'html.parser')

    goal = []
    for wynik in bs.find_all('td', align='left'):
        for c in wynik.find_all('a', class_='main'):
            p = c.find_next('td').find_next('td').find_next('td').find_next(
                'td').find_next('td').find_next('td').get_text().strip()
            goal.append(p)

    return goal


def celuloza():
    URL = 'http://www.90minut.pl/liga/1/liga11211.html'
    page = get(URL)
    bs = BeautifulSoup(page.content, 'html.parser')

    celuloza_dates = []  # terminy mecżów Celulozy
    celuloza_pairs = []

    for wynik in bs.find_all('tr', align='left'):
        for celuloza in wynik.find_all('td', string='  Celuloza Kostrzyn nad Odrą  '):
            for dates in celuloza.parent.find_all('td', width='190'):
                c = dates.get_text()
                celuloza_dates.append(c)
            for pairs in celuloza.parent.find_all('td', width='180'):
                p = pairs.get_text().strip()
                celuloza_pairs.append(p)

    count = 0
    celuloza = []
    for i in range(32):
        # print(
        #     f'{celuloza_pairs[count]} vs {celuloza_pairs[count+1]} dnia {celuloza_dates[i]}')
        c = []
        c.append(celuloza_pairs[count])
        c.append(celuloza_pairs[count+1])
        c.append(celuloza_dates[i])
        celuloza.append(c)
        count += 2

    return celuloza
