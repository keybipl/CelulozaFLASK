from lnp import celuloza19
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

    print(next_game19)

    return next_game19


celuloza19ng()
