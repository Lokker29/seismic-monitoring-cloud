from config import MONGO_DB_HOST, MONGO_DB_USER, MONGO_DB_PASSWORD, DATABASE_NAME, BASE_SEISMIC_COLLECTION
from db import DBClient


def main():
    columns = input("Remove columns: ").split()

    client = DBClient()
    client.create_db(MONGO_DB_HOST, MONGO_DB_USER, MONGO_DB_PASSWORD)

    client.unset(DATABASE_NAME, BASE_SEISMIC_COLLECTION, *columns)


if __name__ == '__main__':
    main()