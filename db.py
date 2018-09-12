#!/usr/bin/evn python
import sqlite3





conn = sqlite3.connect('main.db')
conn.execute('''CREATE TABLE IF NOT EXISTS OTCBTC_TRADES
       (id integer primary key,
       market           TEXT ,
       price           TEXT ,
       volume			TEXT,
       at         TEXT,
       funds TEXT,
       created_at TEXT,
       side TEXT);''')
print "Table created successfully";
conn.commit()
conn.close()



def execute(execFunc):
	conn = sqlite3.connect('main.db');
	result = execFunc(conn);
	conn.commit()
	conn.close();
	return result;


