import sqlite3

connection = sqlite3.connect("next.sqlite")
cursor = connection.cursor()
test = cursor.execute("SELECT home, guest, date, result FROM NextGame WHERE id = 1" ).fetchone()

home = test[0]
guest = test[1]
date = test[2]
result = test[3]

