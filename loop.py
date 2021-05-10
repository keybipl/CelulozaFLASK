from pony.orm import *
import time

db = Database()


class Loop(db.Entity):
    number = Required(int)


db.bind(provider='sqlite', filename='news.db', create_db=True)
db.generate_mapping(create_tables=True)
set_sql_debug(True)

# with db_session:
#     Loop(number=1)


while True:
    with db_session:
        number = Loop[1].number
        Loop[1].number = number + 1
        time.sleep(5)
