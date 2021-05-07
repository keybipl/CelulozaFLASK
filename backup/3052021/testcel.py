from next_game import next_game, last
from pony.orm import *
from datetime import datetime
import time

celuloza = next_game()
celuloza_last = last()
db = Database()

print(celuloza_last)


class NextGame(db.Entity):
    home = Required(str)
    guest = Required(str)
    date = Required(datetime)
    result = Optional(str)


db.bind(provider='sqlite', filename='next.sqlite', create_db=True)
db.generate_mapping(create_tables=True)
set_sql_debug(True)


# with db_session:
#     NextGame(home=celuloza_last[0],
#              guest=celuloza_last[1], date=celuloza_last[2], result=celuloza_last[3])

while True:

    with db_session:
        home = NextGame[1].home
        guest = NextGame[1].guest
        date = NextGame[1].date

    with db_session:
        home_last = NextGame[2].home
        guest_last = NextGame[2].guest
        date_last = NextGame[2].date

    homecel = celuloza[0]
    guestcel = celuloza[1]
    datecel = celuloza[2]

    if home != homecel or guest != guestcel:
        with db_session:
            NextGame[1].home = homecel
            NextGame[1].guest = guestcel
            NextGame[1].date = datecel


    homecel_last = celuloza_last[0]
    guestcel_last = celuloza_last[1]
    datecel_last = celuloza_last[2]
    resultcel_last = celuloza_last[3]

    if home_last != homecel_last or guest_last != guestcel_last:
        with db_session:
            NextGame[2].home = homecel_last
            NextGame[2].guest = guestcel_last
            NextGame[2].date = datecel_last
            NextGame[2].result = resultcel_last

    time.sleep(10)
