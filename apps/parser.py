import json
import requests
import pandas as pd
from datetime import date

from config import PARSER_URL


class Parser:
	base_url = PARSER_URL

	COUNT = 'count'
	QUERY = 'query'

	def _send_request(self, url):
		response = requests.get(url=url)
		return response

	def get_count(self, start=None, end=None, format='geojson'):
		"""
		param start: str in format 'yyyy-mm-dd'
		param end: str in format 'yyyy-mm-dd'
		"""
		method = self.COUNT

		parameters = []

		if start is not None:
			start = start.strftime('%Y-%m-%d') if isinstance(start, date) else start
			parameters.append('starttime=' + start)
		if end is not None:
			end = end.strftime('%Y-%m-%d') if isinstance(end, date) else end
			parameters.append('endtime=' + end)
		if format is not None:
			parameters.append('format=' + format)

		parameters = '&'.join(parameters)

		request_url = self.base_url + method + '?' + parameters

		response = self._send_request(request_url)

		data = json.loads(response.text)

		return data['count']

	def get_count_today(self):
		today = date.today()

		return self.get_count(start=today)

	def get_information(self, start=None, end=None, format='geojson'):
		"""
		param start: str in format 'yyyy-mm-dd'
		param end: str in format 'yyyy-mm-dd'
		"""
		method = self.QUERY

		parameters = []

		if start is not None:
			start = start.strftime('%Y-%m-%d') if isinstance(start, date) else start
			parameters.append('starttime=' + start)
		if end is not None:
			end = end.strftime('%Y-%m-%d') if isinstance(end, date) else end
			parameters.append('endtime=' + end)
		if format is not None:
			parameters.append('format=' + format)

		parameters = '&'.join(parameters)

		request_url = self.base_url + method + '?' + parameters

		response = self._send_request(request_url)

		data = json.loads(response.text)

		pandasDF = pd.DataFrame.from_dict([{
			'coord': feature['geometry']['coordinates'],
			'mag': feature['properties']['mag'],
			'place': feature['properties']['place'],
			'time': feature['properties']['time'],
			'title': feature['properties']['title'],
		} for feature in data['features']])

		pandasDF.dropna(inplace=True)
		return list(pandasDF.T.to_dict().values())

	def get_information_today(self):
		today = date.today()

		return self.get_information(start=today)
