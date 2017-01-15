#!/usr/bin/env python

import cgi

from bs4 import BeautifulSoup

from demo.db_manager import DBManager
from demo.models import Person


manager = DBManager()
fieldnames = ('name', 'age', 'job', 'pay')

form = cgi.FieldStorage()               # parse form data
print('Content-type: text/html\n')      # hdr plus blank line

with open('form.html') as f:
    template = f.read()

soup = BeautifulSoup(template, "html.parser")
form_element = soup.find('form')
form_element.attrs['action'] = 'cgi_script.py'


def fetch(key):
    person = manager.get(key)
    if person is not None:
        for fieldname in fieldnames:
            field = soup.find('input', attrs={'name': fieldname})
            field.attrs['value'] = repr(getattr(person, fieldname))
    else:
        errors = soup.find('p', attrs={'id': 'errors'})
        errors.string = "No such key"


def update(key):
    person_dict = {}
    for fieldname in fieldnames:
        value = form[fieldname].value
        person_dict[fieldname] = eval(value)
        field = soup.find('input', attrs={'name': fieldname})
        field.attrs['value'] = value
    new_person = Person.from_dict(person_dict)
    manager.set(key, new_person)
    success = soup.find('p', attrs={'id': 'success'})
    success.string = "Person updated"


key = form['key'].value
key_field = soup.find('input', attrs={'name': 'key'})
key_field.attrs['value'] = key

action = form['action'].value if 'action' in form else None
if action == 'Fetch':
    fetch(key)
elif action == 'Update':
    update(key)

template = str(soup)
print(template)
