#!/usr/bin/evn python
import db



def create(dataList):

	def createCallback(conn):

		sql = """insert into OTCBTC_TRADES (id,
		   market           ,
		   price           ,
		   volume		,
		   at        ,
		   funds,
		   created_at,
		   side) values (?,?,?,?,?,?,?,?);"""

		if(isinstance(dataList,list)):
			for data in dataList:
				conn.execute(sql,(data["id"],data["market"],data["price"],data["volume"],data["at"],data["funds"],data["created_at"],data["side"]))
		elif (isinstance(dataList,dict)):
			conn.execute(sql,(dataList["id"],dataList["market"],dataList["price"],dataList["volume"],dataList["at"],dataList["funds"],dataList["created_at"],dataList["side"]))

	db.execute(createCallback);


def count(minId,market):
	sql = "select count(1) from OTCBTC_TRADES where id >= ? and market = ?"

	def createCallback(conn):
		cur = conn.cursor().execute(sql,(minId,market));
		for c in cur:
			return c[0];

	return db.execute(createCallback)

