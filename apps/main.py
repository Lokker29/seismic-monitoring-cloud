from datetime import datetime

from ai import create_polynomial_regression_model, predict_by_model_and_data
from config import DATABASE_NAME, BASE_SEISMIC_COLLECTION, ML_MODEL, START_DATE, ML_PREDICT
from db import DBClient
from config import MONGO_DB_HOST, MONGO_DB_USER, MONGO_DB_PASSWORD
from parser import Parser


def prepare_data(data):
    X = list(data.keys())
    Y = list(data.values())

    return X, Y


def save_model(client, model):
    client.set_collection(ML_MODEL)

    client.save_model(model)

    client.set_collection(BASE_SEISMIC_COLLECTION)


def save_predict(client, predict):
    client.set_collection(ML_PREDICT)

    client.save_predict(predict)

    client.set_collection(BASE_SEISMIC_COLLECTION)


def generate_learn_model(client):
    start = datetime.strptime(START_DATE, '%Y-%m-%d')

    data = client.get_data_by_range_date(start=start)

    X, Y = prepare_data(data)
    degree = 2

    model = create_polynomial_regression_model(X, Y, degree=degree)
    save_model(client, model)

    predict = predict_by_model_and_data(model, datetime.now(), degree)
    save_predict(client, predict)


def update_info(parser, client):
    info = parser.get_information_today()
    client.add_to_collection(data=info)


def main():
    client = DBClient()

    client.connect_db(MONGO_DB_HOST, MONGO_DB_USER, MONGO_DB_PASSWORD)

    client.set_db(DATABASE_NAME)
    client.set_collection(BASE_SEISMIC_COLLECTION)

    parser = Parser()

    update_info(parser, client)

    generate_learn_model(client)


if __name__ == '__main__':
    main()
