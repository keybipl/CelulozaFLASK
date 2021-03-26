from bs4 import BeautifulSoup
from requests import get


def game():
    URL = 'https://www.laczynaspilka.pl/rozgrywki/clj,40143.html?round=0'
    page = get(URL)
    bs = BeautifulSoup(page.content, 'html.parser')

    days = []
    for wynik in bs.find_all('span', class_='day'):
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

    # score = []
    # for wynik in bs.find_all('span', class_='score'):
    #     score.append(wynik.get_text().split()[0])
    scores = []
    for wynik in bs.find_all(True, {'class':['score', 'score-empty']}):
        scores.append(wynik.get_text().split()[0])


    # score_empty = []
    # for wynik in bs.find_all('span', class_='score-empty'):
    #     score_empty.append(wynik.get_text().split()[0])


    teams = []
    for wynik in bs.find_all('a', class_='team'):
        teams.append(wynik.get_text())

    count = 0
    games = []

    if len(days) != 56:
        game = False

    else:
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
            c.append(scores[i])
            games.append(c)
            count += 2

    if len(days) != 56:
        game = False

        return game

    else:
        a = 0
        b = 4
        game = []
        for i in range(14):
            game.append(games[a:b])
            a += 4
            b += 4

        return game


def tjm():
    URL = 'https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi-juniorzy,40045.html?round=0'
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


    scores = []
    for wynik in bs.find_all(True, {'class':['score', 'score-empty']}):
        scores.append(wynik.get_text().split()[0])

    # score = []
    # for wynik in bs.find_all('span', class_='score'):
    #     score.append(wynik.get_text().split()[0])

    # score_empty = []
    # for wynik in bs.find_all('span', class_='score-empty'):
    #     score_empty.append(wynik.get_text().split()[0])

    # scores = score + score_empty

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
        c.append(scores[i])
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
    URL = 'https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi-juniorzy,40479.html?round=0'
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

    # score = []
    # for wynik in bs.find_all('span', class_='score'):
    #     score.append(wynik.get_text().split()[0])

    # score_empty = []
    # for wynik in bs.find_all('span', class_='score-empty'):
    #     score_empty.append(wynik.get_text().split()[0])

    # scores = score + score_empty

    scores = []
    for wynik in bs.find_all(True, {'class':['score', 'score-empty']}):
        scores.append(wynik.get_text().split()[0])

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
        c.append(scores[i])
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


def tablejs():
    URL = 'https://www.laczynaspilka.pl/rozgrywki-tabela/clj,40143.html'
    page = get(URL)
    bs = BeautifulSoup(page.content, 'html.parser')

    teams = []
    for wynik in bs.find_all('a', class_='team'):
        teams.append(wynik.get_text())

    points = []
    for wynik in bs.find_all('div', class_='grids-wrapper'):
        points.append(wynik.get_text().split())

    points.remove(points[0])
    points.remove(points[0])
    points.remove(points[0])
    points.remove(points[0])

    punktyjs = []
    for i in range(0, 32):
        if i in (0, 4, 8, 12, 16, 20, 24, 28):
            punktyjs.append(points[i])

    return punktyjs, teams


def tablejm():
    URL = 'https://www.laczynaspilka.pl/rozgrywki-tabela/nizsze-ligi-juniorzy,40045.html'
    page = get(URL)
    bs = BeautifulSoup(page.content, 'html.parser')

    teamsjm = []
    for wynik in bs.find_all('a', class_='team'):
        teamsjm.append(wynik.get_text())

    points = []
    for wynik in bs.find_all('div', class_='grids-wrapper'):
        points.append(wynik.get_text().split())

    points.remove(points[0])
    points.remove(points[0])
    points.remove(points[0])
    points.remove(points[0])

    punktyjm = []
    for i in range(0, 32):
        if i in (0, 4, 8, 12, 16, 20, 24, 28):
            punktyjm.append(points[i])

    return punktyjm, teamsjm


def tabletr():
    URL = 'https://www.laczynaspilka.pl/rozgrywki-tabela/nizsze-ligi-juniorzy,40479.html'
    page = get(URL)
    bs = BeautifulSoup(page.content, 'html.parser')

    teamstr = []
    for wynik in bs.find_all('a', class_='team'):
        teamstr.append(wynik.get_text())

    points = []
    for wynik in bs.find_all('div', class_='grids-wrapper'):
        points.append(wynik.get_text().split())

    points.remove(points[0])
    points.remove(points[0])
    points.remove(points[0])
    points.remove(points[0])

    punktytr = []
    for i in range(0, 32):
        if i in (0, 4, 8, 12, 16, 20, 24, 28):
            punktytr.append(points[i])

    return punktytr, teamstr
