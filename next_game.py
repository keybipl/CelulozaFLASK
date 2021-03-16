from minut import celuloza
import datetime

# miesiące przyporządkowane do liczby
konwersja = {

    'sierpnia': 8,
    'września': 9,
    'października': 10,
    'listopada': 11,
    'grudnia': 12,
    'stycznia': 1,
    'lutego': 2,
    'marca': 3,
    'kwietnia': 4,
    'maja': 5,
    'czerwca': 6,
    'lipca': 7,

}

# miesiące przyporządkowane do roku
rok = {

    'lipca': 2020,
    'sierpnia': 2020,
    'września': 2020,
    'października': 2020,
    'listopada': 2020,
    'grudnia': 2020,
    'stycznia': 2021,
    'lutego': 2021,
    'marca': 2021,
    'kwietnia': 2021,
    'maja': 2021,
    'czerwca': 2021,

}


def last():
    dane = celuloza()
    # print(datetime.datetime.now())
    # print(dane)

    for i in range(32):
        test = dane[i][2].replace(',', '')
        dane[i][2] = test
        # print(dane[i][2])

    lista = []
    for i in range(32):
        data = dane[i][2].split(' ')
        if len(data) > 1:
            year = int(rok[data[1]])
            month = int(konwersja[data[1]])
            day = int(data[0])
            hour = data[2].split(':')
            hourh = int(hour[0])
            minutes = int(hour[1])
            date = datetime.datetime(year, month, day, hourh, minutes)
            date_now = datetime.datetime.now()
            if date < date_now:
                last = [dane[i][0], dane[i][1], date, dane[i][3]]
                lista.append(last)

    last = lista[-1]

    return last


def next_game():
    dane = celuloza()
    # print(datetime.datetime.now())
    # print(dane)

    for i in range(32):
        test = dane[i][2].replace(',', '')
        dane[i][2] = test
        # print(dane[i][2])

    lista = []
    for i in range(32):
        data = dane[i][2].split(' ')
        if len(data) > 1:
            year = int(rok[data[1]])
            month = int(konwersja[data[1]])
            day = int(data[0])
            hour = data[2].split(':')
            hourh = int(hour[0])
            minutes = int(hour[1])
            date = datetime.datetime(year, month, day, hourh, minutes)
            date_now = datetime.datetime.now()
            if date > date_now:
                next_game = [dane[i][0], dane[i][1], date, dane[i][3]]
                lista.append(next_game)
        else:
            next_game = dane[i]
            lista.append(next_game)

    next_game = lista[0]

    return next_game
