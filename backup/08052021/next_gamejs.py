from lnp import celuloza19, celulozajm, celulozatr
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