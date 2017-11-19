import requests
import keys
import time


nonce = int(time.time()*100)
data = {
	'clientId': keys.id,
	'publicKey': keys.public,
	'nonce': nonce,
	'signature': keys.createSignature(keys.id, keys.public, keys.private, nonce)
}
r = requests.post("https://coinmate.io/api/balances", data = data)
print r.text

nonce = int(time.time()*100)
data = {
	'offset': 0,
	'limit': 30,
	'clientId': keys.id,
	'publicKey': keys.public,
	'nonce': nonce,
	'signature': keys.createSignature(keys.id, keys.public, keys.private, nonce)
}
r = requests.post("https://coinmate.io/api/transactionHistory", data = data)
print r.text