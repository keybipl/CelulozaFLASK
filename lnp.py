from bs4 import BeautifulSoup
from requests import get


def game():
    URL = 'https://www.laczynaspilka.pl/rozgrywki/clj,40143.html?fbclid=IwAR0oFhnwxKSpmNgwn18WXzWohxRw1gbKdzAc2CoXgiYwZZ6fdqOLI7bInNY'
    page = get(URL)
    bs = BeautifulSoup(page.content, 'html.parser')

    days = []
    count = 1
    for wynik in bs.find_all('span', class_='day'):
        count += 1
        days.append(wynik.get_text())

    months = []
    year = []
    for wynik in bs.find_all('span', class_='month'):
        a = str(wynik.get_text())
        b = a.replace('/', ' ')
        c = b.split()
        months.append(c[0])
        year.append(c[1])

    hour = []
    for wynik in bs.find_all('span', class_='hour'):
        hour.append(wynik.get_text())

    teams = []
    for wynik in bs.find_all('a', class_='team'):
        teams.append(wynik.get_text())

    count = 0
    games = []
    for i in range(56):
        # print(
        #     f'{days[i]}.{months[i]}.{year[i]}, g. {hour[i]} - {teams[count]} vs {teams[count+1]}')
        c = []
        c.append(days[i])
        c.append(months[i])
        c.append(year[i])
        c.append(hour[i])
        c.append(teams[count])
        c.append(teams[count+1])
        games.append(c)
        count += 2

    a = 0
    b = 4
    game = []
    for i in range(14):
        game.append(games[a:b])
        a += 4
        b += 4

    return game


def tjm():
    URL = 'https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi-juniorzy,40045.html'
    page = get(URL)
    bs = BeautifulSoup(page.content, 'html.parser')

    days = []
    count = 1
    for wynik in bs.find_all('span', class_='day'):
        count += 1
        days.append(wynik.get_text())

    months = []
    year = []
    for wynik in bs.find_all('span', class_='month'):
        a = str(wynik.get_text())
        b = a.replace('/', ' ')
        c = b.split()
        months.append(c[0])
        year.append(c[1])

    hour = []
    for wynik in bs.find_all('span', class_='hour'):
        hour.append(wynik.get_text())

    teams = []
    for wynik in bs.find_all('a', class_='team'):
        teams.append(wynik.get_text())

    count = 0
    games = []
    for i in range(56):
        # print(
        #     f'{days[i]}.{months[i]}.{year[i]}, g. {hour[i]} - {teams[count]} vs {teams[count+1]}')
        c = []
        c.append(days[i])
        c.append(months[i])
        c.append(year[i])
        c.append(hour[i])
        c.append(teams[count])
        c.append(teams[count+1])
        games.append(c)
        count += 2

    a = 0
    b = 4
    tjm = []
    for i in range(14):
        tjm.append(games[a:b])
        a += 4
        b += 4

    return tjm


def tr():
    URL = 'https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi-juniorzy,40479.html'
    page = get(URL)
    bs = BeautifulSoup(page.content, 'html.parser')

    days = []
    count = 1
    for wynik in bs.find_all('span', class_='day'):
        count += 1
        days.append(wynik.get_text())

    months = []
    year = []
    for wynik in bs.find_all('span', class_='month'):
        a = str(wynik.get_text())
        b = a.replace('/', ' ')
        c = b.split()
        months.append(c[0])
        year.append(c[1])

    hour = []
    for wynik in bs.find_all('span', class_='hour'):
        hour.append(wynik.get_text())

    teams = []
    for wynik in bs.find_all('a', class_='team'):
        teams.append(wynik.get_text())

    count = 0
    games = []
    for i in range(56):
        # print(
        #     f'{days[i]}.{months[i]}.{year[i]}, g. {hour[i]} - {teams[count]} vs {teams[count+1]}')
        c = []
        c.append(days[i])
        c.append(months[i])
        c.append(year[i])
        c.append(hour[i])
        c.append(teams[count])
        c.append(teams[count+1])
        games.append(c)
        count += 2

    a = 0
    b = 4
    tr = []
    for i in range(14):
        tr.append(games[a:b])
        a += 4
        b += 4

    return tr
