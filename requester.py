import time
import hmac
import hashlib
import requests

class Requester(object):

	def __init__(self, id, private, public, currency):
		self.id = id
		self.private = private
		self.public = public
		self.currency = currency

	def create_signature(self, nonce):
		message = str(nonce) + str(self.id) + self.public
		signature = hmac.new(self.private, message, digestmod=hashlib.sha256).hexdigest()
		return signature.upper()

	def prepare_post_data(self):
		nonce = int(time.time()*100)
		return {
			'clientId': self.id,
			'publicKey': self.public,
			'nonce': nonce,
			'signature': self.create_signature(nonce)
		}

	def get_ticker(self):
		return requests.get('https://coinmate.io/api/ticker?currencyPair=' + self.curency)

	def get_balance(self):
		data = self.prepare_post_data()
		return requests.post("https://coinmate.io/api/balances", data = data)

	def get_history(self, offset=0, limit=100):
		data = self.prepare_post_data()
		data.update({
			'offset': offset,
			'limit': limit,
		})
		return requests.post("https://coinmate.io/api/transactionHistory", data = data)
