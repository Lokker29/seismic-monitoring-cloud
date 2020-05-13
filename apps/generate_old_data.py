from config import DATABASE_NAME, BASE_SEISMIC_COLLECTION, MONGO_DB_HOST, MONGO_DB_USER, MONGO_DB_PASSWORD
from db import DBClient
from parser import Parser


def update_info(parser, client, start, end):
    info = parser.get_information(start, end)
    client.add_to_collection(DATABASE_NAME, BASE_SEISMIC_COLLECTION, data=info)


def main():
    client = DBClient()

    client.create_db(MONGO_DB_HOST, MONGO_DB_USER, MONGO_DB_PASSWORD)

    parser = Parser()

    start = input("Start (yyyy-mm-nn): ")
    end = input("End (yyyy-mm-dd): ")

    update_info(parser, client, start, end)


if __name__ == '__main__':
    main()
