from datetime import datetime

from pymongo import MongoClient

TIME_CONSTANT = 1e3


def mean_list(data):
    return sum(data) / len(data)


class DBClient:
    client = None
    db = None
    collection = None

    def connect_db(self, host, user, password):
        self.client = MongoClient(
            host=host,
            username=user,
            password=password,
        )

    def set_db(self, name):
        self.db = self.client[name]

    def set_collection(self, name):
        self.collection = self.db[name]

    def add_to_collection(self, data):
        if self.client is None:
            print("Implement client!")
            return

        if isinstance(data, list):
            self.collection.insert_many(data)
        elif isinstance(data, dict):
            self.collection.insert_one(data)

    def unset(self, *columns):
        self.collection.update({}, {'$unset': {col: 1 for col in columns}}, multi=True)

    def _statistic_of_magnitude_by_date(self, data):
        statistic = {}

        for row in data:
            day = int(row['time'] / TIME_CONSTANT / (60 * 60 * 24))
            statistic[day] = statistic.get(day, []) + [row['mag']]

        statistic = {date_: mean_list(mags) for date_, mags in statistic.items()}

        return dict(sorted(statistic.items(), key=lambda x: x[0]))

    def get_data_by_range_date(self, start, end=None):
        start = start.timestamp() * TIME_CONSTANT

        if end is None:
            end = datetime.today().timestamp() * TIME_CONSTANT

        columns = ('time', 'mag')

        data = self.collection.find(filter={'time': {'$gte': start, '$lt': end}},
                                    projection={column: 1 for column in columns},).sort('time')

        data = self._statistic_of_magnitude_by_date(data)

        min_val = list(data.keys())[0]
        data = {key - min_val: val for key, val in data.items()}

        return data

    def save_model(self, model):
        self.collection.remove({})

        model_param = {}
        model_param['coef'] = list(model.coef_)
        model_param['intercept'] = model.intercept_.tolist()

        self.collection.insert_one({'ml_model': model_param})
