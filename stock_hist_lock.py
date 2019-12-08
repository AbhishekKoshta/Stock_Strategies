import time
st = time.clock()
from nsetools import Nse
from datetime import date
from nsepy import get_history

nse = Nse()

all_stock_codes = nse.get_stock_codes()
count=0
for stk in all_stock_codes:
	count+=1
	print (count,stk)
	try:
		stock = get_history(symbol=stk,
		                   start=date(2019,10,2),
		                   end=date(2019,12,6))
	except:
		print ("Problem finding data for",stk)

	stock.to_csv("C:\\Python27\\Stock Market\\Working\\Stocks_NSE\\{}.csv".format(stk))

print (time.clock()-st)