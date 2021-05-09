from lnp import celuloza19, celulozajm, celulozatr
from next_game import next_game
import datetime


def celuloza19ng():
    celuloza = celuloza19()
    date_now = datetime.datetime.now()

    celulozang = []
    for game in celuloza:
        date = game[0]
        if date > date_now:
            g = [date, game[1], game[2], game[3], game[4]]
            celulozang.append(g)

    next_games = [elem for elem in celulozang if elem[0]]
    next_rival = sorted(next_games, key=lambda x: x[0])

    # print(next_rival)

    next_game19 = next_rival[0]

    return next_game19


def celulozajmng():
    celuloza = celulozajm()
    date_now = datetime.datetime.now()

    celulozang = []
    for game in celuloza:
        date = game[0]
        # print(date)
        if date > date_now:
            g = [date, game[1], game[2], game[3], game[4]]
            celulozang.append(g)

    next_rival = sorted(celulozang, key=lambda x: x[0])

    # print(next_rival)

    next_gamejm = next_rival[0]

    # print(next_gamejm)

    return next_gamejm


def celulozatrng():
    celuloza = celulozatr()
    date_now = datetime.datetime.now()

    celulozang = []
    for game in celuloza:
        date = game[0]
        # print(date)
        if date > date_now:
            g = [date, game[1], game[2], game[3], game[4]]
            celulozang.append(g)

    next_rival = sorted(celulozang, key=lambda x: x[0])

    next_gametr = next_rival[0]

    return next_gametr


def today():
    sen = next_game()
    js = celuloza19ng()
    jm = celulozajmng()
    tr = celulozatrng()
    date_now = datetime.datetime.now()
    datesen = sen[2]
    datejs = js[0]
    datejm = jm[0]
    datetr = tr[0]
    today = []
    if datesen.year == date_now.year and datesen.month == date_now.month and datesen.day == date_now.day:
        senng = True
        # js.append('js')
        # today.append(js)
    else:
        senng = False
    if datejs.year == date_now.year and datejs.month == date_now.month and datejs.day == date_now.day:
        jsng = True
        # js.append('js')
        # today.append(js)
    else:
        jsng = False
    if datejm.year == date_now.year and datejm.month == date_now.month and datejm.day == date_now.day:
        jmng = True
        # jm.append('jm')
        # today.append(jm)
    else:
        jmng = False
    if datetr.year == date_now.year and datetr.month == date_now.month and datetr.day == date_now.day:
        trng = True
        # tr.append('tr')
        # today.append(tr)
    else:
        trng = False

    # print(senng, jsng, jmng, trng)

    return [senng, jsng, jmng, trng]


# today()
