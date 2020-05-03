from datetime import date

from config import DATABASE_NAME, BASE_SEISMIC_COLLECTION
from db import DBClient
from config import MONGO_DB_HOST, MONGO_DB_USER, MONGO_DB_PASSWORD
from parser import Parser


def update_info(parser, client):
    info = parser.get_information_today()
    client.add_to_collection(DATABASE_NAME, BASE_SEISMIC_COLLECTION, data=info)


def update_count(parser, client):
    count = parser.get_count_today()
    count_info = {'count': count, 'date': date.today().strftime('%Y-%m-%d')}
    client.add_to_collection(DATABASE_NAME, 'seismic-count', data=count_info)


def main():
    client = DBClient()

    client.create_db(MONGO_DB_HOST, MONGO_DB_USER, MONGO_DB_PASSWORD)

    parser = Parser()

    update_info(parser, client)
    update_count(parser, client)


if __name__ == '__main__':
    main()
