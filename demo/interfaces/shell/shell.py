import sys

from demo.db_manager import DBManager
from demo.models import Person


def person_list():
    manager = DBManager()
    dbdata = manager.load_db()
    for key, value in dbdata.items():
        print("{key}: {value}".format(key=key, value=value))


def person_get():
    try:
        key = sys.argv[1]
    except IndexError:
        print("Provide a key")
        return
    manager = DBManager()
    person = manager.get(key)
    if person:
        print(person)
    else:
        print("Person not found")


def person_add():
    try:
        key = sys.argv[1]
    except IndexError:
        print("Provide a key")
        return
    manager = DBManager()
    exists = manager.get(key)
    if exists:
        print("Key already exists")
    fields = dict.fromkeys(('name', 'age', 'job', 'pay'))
    for f in fields:
        value = input('enter {}: '.format(f))
        fields[f] = eval(value)
    person = Person.from_dict(fields)
    manager.set(key, person)
    print("New person is added:", person)
