import tradeService
import logging

#logging setting

logging.basicConfig(filename = "otcbtc.log",level = logging.INFO)




if __name__ == '__main__':



	f = open("market.list")
	marketsStr = f.read()
	markets =  marketsStr.split("\n")
	#markets = ["trxeth"]
	while True:
		for market in markets:
			tradeService.create(market)
		pass