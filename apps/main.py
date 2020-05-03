from config import DATABASE_NAME, BASE_SEISMIC_COLLECTION
from db import DBClient
from config import MONGO_DB_HOST, MONGO_DB_USER, MONGO_DB_PASSWORD


if __name__ == '__main__':
    client = DBClient()

    client.create_db(MONGO_DB_HOST, MONGO_DB_USER, MONGO_DB_PASSWORD)
