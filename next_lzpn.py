from bs4 import BeautifulSoup
from requests import get
import datetime


def next_game():
    URLt = 'http://www.lubuskizpn.pl/extranet/?action=getTimeSchedulesList&play_id=36712'
    trampkarze = get(URLt)
    bst = BeautifulSoup(trampkarze.content, 'html.parser')

    wyniki = []
    for wynik in bst.find_all('tr'):
        if wynik.find_all('td', string='TS CELULOZA  KOSTRZYN  n/o'):
            w = wynik.get_text().strip()
            wyniki.append(w)

    lista = []
    for i in range(len(wyniki)):
        string = str([wyniki[i]])
        a = string.replace(r'\n', '?'). replace(
            '[', '').replace('\'', '').replace(']', '')
        a = a.split('?')
        lista.append(a)

    # print(lista)

    next_game = []
    for elem in lista:
        if elem[3] == 'TS CELULOZA  KOSTRZYN  n/o':
            elem[3] = 'TS Celuloza'
        if elem[5] != 'b/d':
            year = int(elem[4][0:4])
            month = int(elem[4][5:7])
            day = int(elem[4][8:10])
            hour = int(elem[5][0:2])
            minutes = int(elem[5][3:5])
            date = datetime.datetime(year, month, day, hour, minutes)
            date_now = datetime.datetime.now()
            next_match = []
            if date > date_now:
                next_match.append(elem[0])
                next_match.append(elem[3])
                next_match.append(date)
                next_game.append(next_match)

    next_rival = sorted(next_game, key=lambda x: x[2])

    next_game = next_rival[0]

    return next_game
