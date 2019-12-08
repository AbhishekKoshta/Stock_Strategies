# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 08:16:50 2019

@author: ayuan
"""

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
all_stock_codes = pd.read_csv("all_stock_codes.csv")
#all_stock_codes = pd.read_csv("fno.csv")

for stk in range(len(all_stock_codes)):
	stock =  all_stock_codes['0'][stk]
#	stock =  all_stock_codes['Code'][stk]    
# for stock in all_stock_codes:
	count+=1
	print (count,stock)
	if stock == "SYMBOL" or stock=="COMPANY":
		continue
	try:
		st_read = pd.read_csv("C:\\Python27\\Stock Market\\Working\\Stocks_NSE\\{}.csv".format(stock))
	except:
		continue
    # print (st_read)
    # Parameters to be changed
	days = len(st_read['High']); atr_brk_v=2; atr_brk = 3
	n = 8 #days; atr_brk_v
    
	try:
		ATR = st_read['High'][::-1][:n][1:] - st_read['Low'][::-1][:n][1:]
		ATR = ATR.mean()
		SMAV = st_read['Volume'][::-1][:n][1:].mean()
		atr_break_u = st_read['Last'][days-2] + ATR*atr_brk
		atr_break_d = st_read['Last'][days-2] - ATR*atr_brk
	except:
		continue
	if st_read['Last'][days-1] > atr_break_u:
		if st_read['Volume'][days-1] > SMAV*atr_brk_v:
			brk_list.append((stock,st_read["Last"][days-1],"Up"))
			print ("=================Buy this stock=============",stock)

	if st_read['Last'][days-1] < atr_break_d:
		if st_read['Volume'][days-1] > SMAV*atr_brk_v:
			brk_list.append((stock,st_read["Last"][days-1],"Down"))
			print ("=================Sell this stock=============",stock)

sbrk_list = set(brk_list)
print (set(brk_list), len(brk_list))
pd.DataFrame(sbrk_list).to_csv("{}.csv".format(date.today()))
print ("Time taken in secs",time.clock()-st)