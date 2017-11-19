import requests
import keys
import time
import mock_history

r = keys.Requester(id=keys.id, private=keys.private, public=keys.public, currency='LTC_BTC')

# print r.get_history().text
history = mock_history.history

filtered = [move for move in history['data'] if move['priceCurrency']=='BTC' and move['amountCurrency']=='LTC']

last = None
buckets = []
for move in filtered:
	move.update({'total':move['price']*move['amount']})
	if not last:
		last = move.copy()
		continue
	if (last['transactionType'] == move['transactionType']
		and last['price'] == move['price']):
		last['amount'] += move['amount']
		print last
	else:
		last.update({'total':last['price']*last['amount']})
		buckets.append(last)
		last = move.copy()



for move in filtered:
	print '%(transactionType)4s   %(amount)0.5f %(amountCurrency)s   %(price)3.5f %(priceCurrency)s   %(total)f' % move

print "buckets"
for move in buckets:
	print '%(transactionType)4s   %(amount)3.5f %(amountCurrency)s   %(price)3.5f %(priceCurrency)s   %(total)f' % move