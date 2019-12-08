import time
st = time.clock()
from nsetools import Nse
import pandas as pd
import time
from datetime import date
nse = Nse()

# all_stock_codes = nse.get_stock_codes()
# all_stock_codes = list(all_stock_codes.keys())
brk_list=[]
# pd.DataFrame.from_dict(all_stock_codes, orient = 'index').to_csv('all_stock_codes.csv',index=False)
# pd.DataFrame((all_stock_codes)).to_csv('all_stock_codes.csv',index=False)
# n = 15 #Days
# all_stock_codes = pd.read_csv("all_stock_codes.csv")
count=1
all_stock_codes = pd.read_csv("fno.csv")
for stk in range(len(all_stock_codes)):
	stock =  all_stock_codes['Code'][stk]
# for stock in all_stock_codes:
	count+=1
	print (count,stock)
	if stock == "SYMBOL" or stock=="COMPANY":
		continue
	st_read = pd.read_csv("C:\\Python27\\Stock Market\\Working\\Stocks_NSE\\{}.csv".format(stock))
	# print (st_read)
	for n in range(10,16):
		try:
			x,y = max(st_read['High'][::-1][:n][1:]) , min(st_read['Low'][::-1][:n][1:])
			# print (x,y)
			vol = st_read['Volume'][::-1][:n][1:].mean()
		except:
			# print ("============Failure2==============")
			continue

		try:
			# temp = 42
			temp = len(st_read)-1
			close = st_read['Last'][temp]
			high = st_read['High'][temp]
			low = st_read['Low'][temp]
			ope = st_read['Open'][temp]
			last_vol = st_read['Volume'][temp]
			# print (close,high,low,ope,last_vol)
		except:
			# print ("============Failure3==============")
			continue

		if close>x and last_vol > vol*1.3:
			if low >= ope*0.993 and high <= close*1.007:
				print (n,"days breakout pattern=========",stock,close, "==========UP======")
				brk_list.append((stock,close,"Up"))
		elif close<y and last_vol > vol*1.3:
			if low >= ope*0.993 and high <= close*1.007:
				print (n,"days breakout pattern=========",stock,close, "==========")
				brk_list.append((stock,close,"Down"))
sbrk_list = set(brk_list)
print (set(brk_list), len(brk_list))
pd.DataFrame(sbrk_list).to_csv("fno_{}.csv".format(date.today()))
print (time.clock()-st)