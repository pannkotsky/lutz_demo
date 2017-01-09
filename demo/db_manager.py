import shelve

from demo import settings


class DBManager:
    def __init__(self, dbfilename=settings.DBFILENAME):
        self.dbfilename = dbfilename

    def get(self, key):
        """Get item from the store by the given key"""
        with shelve.open(self.dbfilename) as db:
            return db.get(key)

    def set(self, key, item):
        """Add or update item under the given key"""
        with shelve.open(self.dbfilename) as db:
            db[key] = item

    def remove(self, key):
        """Remove item from the store by the given key if it exists"""
        with shelve.open(self.dbfilename) as db:
            if key in db:
                db.pop(key)

    def store_db(self, dbdata, update=False):
        """
        Store data to a file storage

        :param dbdata: dict of dicts, data to store in database
        :param update: bool, whether to update old data in the storage or drop
        it and create new db from scratch
        :return: None
        """

        with shelve.open(self.dbfilename) as db:
            if not update:
                db.clear()
            db.update(dbdata)

    def load_db(self):
        """
        Restore data from file storage reconstructing the db

        :return: dict of dicts, data loaded from database
        """

        with shelve.open(self.dbfilename) as db:
            dbdata = {}
            dbdata.update(db)
            return dbdata


if __name__ == '__main__':
    from demo.initdata import db
    from demo.models import Person

    manager = DBManager()
    manager.store_db(db)
    print(manager.load_db())

    sue = manager.get('sue')
    print(sue)
    print(sue.to_dict())
    sue.age = 40
    manager.set('sue', sue)

    print(manager.get('sue'))

    d = {'name': 'Rob', 'age': 25}
    rob = Person.from_dict(d)
    db = {'rob': rob}
    manager.store_db(db, update=True)
    print(manager.load_db())
