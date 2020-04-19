from pymongo import MongoClient

from config import DATABASE_NAME, MONGO_DB_URL, BASE_SEISMIC_COLLECTION

if __name__ == '__main__':
    client = MongoClient(MONGO_DB_URL)

    db = client[DATABASE_NAME]
    # db.authenticate('root', '23052019')

    collection = db[BASE_SEISMIC_COLLECTION]

    print("Start")
    first = collection.insert_one({'a': 1}).inserted_id
    print(first)
    print("Done")
