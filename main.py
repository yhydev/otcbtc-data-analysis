#!/usr/bin/env python
import logging
logging.basicConfig(filename = "otcbtc.log",level = logging.INFO,datefmt = "%Y-%m-%d %H:%M:%S",format = "%(asctime)s %(levelname)s\t: %(message)s")
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
