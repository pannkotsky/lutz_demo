import shelve

DBFILENAME = 'people-file'


def add_item(key, item, dbfilename=DBFILENAME):
    """Add item to storage under the given key"""
    db = shelve.open(dbfilename)
    db[key] = item
    db.close()


def store_db(dbdata, dbfilename=DBFILENAME, update=False):
    """
    Store data to a file storage

    :param dbdata: dict of dicts, data to store in database
    :param dbfilename: str, name of the storage file
    :param update: bool, whether to update old data in the storage or drop it
    :return: None
    """

    db = shelve.open(dbfilename)
    if not update:
        db.clear()
    db.update(dbdata)
    db.close()


def load_db(dbfilename=DBFILENAME):
    """
    Restore data from file storage reconstructing the db

    :param dbfilename: str, name of the storage file
    :return: dict of dicts, data loaded from database
    """

    db = shelve.open(dbfilename)
    dbdata = {}
    dbdata.update(db)
    db.close()
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
