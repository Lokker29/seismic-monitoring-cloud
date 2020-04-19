from pymongo import MongoClient

from config import DATABASE_NAME, BASE_SEISMIC_COLLECTION, MONGO_DB_USER, MONGO_DB_PASSWORD, MONGO_DB_HOST

if __name__ == '__main__':
    client = MongoClient(
        host=MONGO_DB_HOST,
        username=MONGO_DB_USER,
        password=MONGO_DB_PASSWORD,
    )

    db = client[DATABASE_NAME]

    collection = db[BASE_SEISMIC_COLLECTION]

    print("Start")
    first = collection.insert_one({'a': 1}).inserted_id
    print("Done")
