from .models import Person


bob = Person('Bob Smith', age=42, pay=30000, job='dev')
sue = Person('Sue Jones', age=45, pay=40000, job='hdw')
tom = Person('Tom', age=50)

db = {}

db['bob'] = bob
db['sue'] = sue
db['tom'] = tom
