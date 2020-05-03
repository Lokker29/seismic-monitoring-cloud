from config import DATABASE_NAME, BASE_SEISMIC_COLLECTION
from db import DBClient
from config import MONGO_DB_HOST, MONGO_DB_USER, MONGO_DB_PASSWORD
from parser import Parser


def main():
    client = DBClient()

    client.create_db(MONGO_DB_HOST, MONGO_DB_USER, MONGO_DB_PASSWORD)

    parser = Parser()

    info = parser.get_information_today()

    client.add_to_collection(DATABASE_NAME, BASE_SEISMIC_COLLECTION, data=info)


if __name__ == '__main__':
    main()
