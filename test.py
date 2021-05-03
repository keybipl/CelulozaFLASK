from pony.orm import *

db = Database()


class Person(db.Entity):
    name = Required(str)
    age = Required(int)
    cars = Set('Car')
    houses = Set('House')


class Car(db.Entity):
    make = Required(str)
    model = Required(str)
    owner = Required(Person)


class House(db.Entity):
    location = Required(str)
    value = Required(int)
    owner = Required(Person)


db.bind(provider='sqlite', filename='houses.db', create_db=True)
db.generate_mapping(create_tables=True)
set_sql_debug(True)


@db_session
def print_person_name(person_id):
    p = Person[person_id]
    print(p.name)
    print(p.age)
    # database session cache will be cleared automatically
    # database connection will be returned to the pool


@db_session
def add_person(name, age):
    Person(name=name, age=age)
    # commit() will be done automatically
    # database session cache will be cleared automatically
    # database connection will be returned to the pool


@db_session
def add_car(person_id, make, model):
    Car(make=make, model=model, owner=Person[person_id])


with db_session:
    p = Person(name='Kate', age=33)
    Car(make='Audi', model='R8', owner=p)
    # commit() will be done automatically
    # database session cache will be cleared automatically
    # database connection will be returned to the pool
