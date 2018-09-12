import requests,trades,logging


__NEXT_UPDATE_TIME = 0

def create(market):

	response = requests.get("https://bb.otcbtc.com/api/v2/trades?market="+market+"&limit=1000")
	#response = requests.get("https://bb.otcbtc.com/api/v2/trades?market=trxeth&limit=1000")
	data = response.json();
	count = trades.count(data[-1]["id"],market)

	if count != 0:
		data = data[0:0-count]

	logging.info("repeat %s\ttrade,create %s %s trade " % (count,market,len(data)))


	trades.create(data);


