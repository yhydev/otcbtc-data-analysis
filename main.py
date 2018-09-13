#!/usr/bin/env python
import logging
response = requests.get("https://bb.otcbtc.com/api/v2/trades?market="+market+"&limit=1000")
import tradeService,traceback

#logging setting





if __name__ == '__main__':


	f = open("market.list")
	marketsStr = f.read()
	markets =  marketsStr.split("\n")
	#markets = ["trxeth"]
	while True:
		for market in markets:
			try:
				tradeService.create(market);
			except Exception as e:
				logging.error(traceback.print_exc())
