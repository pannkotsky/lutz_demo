import shelve

DBFILENAME = 'people-file'


def get(key, dbfilename=DBFILENAME):
    """Get item from the store by the given key"""
    with shelve.open(dbfilename) as db:
        return db.get(key)


def set(key, item, dbfilename=DBFILENAME):
    """Add or update item under the given key"""
    with shelve.open(dbfilename) as db:
        db[key] = item


def remove(key, dbfilename=DBFILENAME):
    """Remove item from the store by the given key if it exists"""
    with shelve.open(dbfilename) as db:
        if key in db:
            db.pop(key)


def store_db(dbdata, dbfilename=DBFILENAME, update=False):
    """
    Store data to a file storage

    :param dbdata: dict of dicts, data to store in database
    :param dbfilename: str, name of the storage file
    :param update: bool, whether to update old data in the storage or drop it
    :return: None
    """

    with shelve.open(dbfilename) as db:
        if not update:
            db.clear()
        db.update(dbdata)


def load_db(dbfilename=DBFILENAME):
    """
    Restore data from file storage reconstructing the db

    :param dbfilename: str, name of the storage file
    :return: dict of dicts, data loaded from database
    """

    with shelve.open(dbfilename) as db:
        dbdata = {}
        dbdata.update(db)
        return dbdata


if __name__ == '__main__':
    from demo.initdata import db
    store_db(db)
    print(load_db())

    db = shelve.open(DBFILENAME)
    print(db['sue'])
    sue = db['sue']
    sue['age'] = 40
    db['sue'] = sue
    db.close()

    db = shelve.open(DBFILENAME)
    print(db['sue'])
    db.close()

    rob = {'name': 'Rob', 'age': 25, 'pay': 100000, 'job': 'fucher'}
    db = {'rob': rob}
    store_db(db, update=True)
    print(load_db())
