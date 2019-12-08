import time
st = time.clock()
from nsetools import Nse
from datetime import date
from nsepy import get_history
import pandas as pd
nse = Nse()

# all_stock_codes = nse.get_stock_codes()
all_stock_codes = pd.read_csv("fno.csv")
# pri/t ()
count=0
for stk in range(len(all_stock_codes)):
	count+=1
	stk = all_stock_codes['Code'][stk]
	try:
		stock = get_history(symbol=stk,
		                   start=date(2010,11,1),
		                   end=date(2019,12,6))
		print (count,stock,stock["Prev Close"][-1])
	except:
		print ("Problem finding data for",stk)
	stock.to_csv("C:\\Python27\\Stock Market\\Working\\FO_Stocks_NSE\\{}.csv".format(stk))

print (time.clock()-st)
