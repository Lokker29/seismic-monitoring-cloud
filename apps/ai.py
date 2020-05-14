from datetime import datetime

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

from config import START_DATE


def create_polynomial_regression_model(X_train, Y_train, degree):
    poly_features = PolynomialFeatures(degree=degree)

    X_train = np.array(X_train).reshape((len(X_train), 1))

    X_train_poly = poly_features.fit_transform(X_train)

    poly_model = LinearRegression()
    poly_model.fit(X_train_poly, Y_train)

    return poly_model


def predict_by_model_and_data(model, date, degree):
    date = int((date.timestamp() - datetime.strptime(START_DATE, '%Y-%m-%d').timestamp()) / (60 * 60 * 24))

    poly_features = PolynomialFeatures(degree=degree)
    date = [[date]]

    date = poly_features.fit_transform(date)

    predict = model.predict(date)

    return list(predict)[0]
