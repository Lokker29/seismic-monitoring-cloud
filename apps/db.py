from pymongo import MongoClient


class DBClient:

	client = None

	def create_db(self, host, user, password):
		self.client = MongoClient(
			host=host,
			username=user,
			password=password,
		)

	def add_to_collection(self, db_name, collection_name, data):
		if self.client is None:
			print("Implement client!")
			return
		db = self.client[db_name]

		collection = db[collection_name]

		if isinstance(data, list):
			collection.insert_many(data)
		elif isinstance(data, dict):
			collection.insert_one(data)
