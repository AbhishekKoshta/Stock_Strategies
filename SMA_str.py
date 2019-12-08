# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 08:16:50 2019
This strategy considers 3 dojis followed by a maribozu and volume breadown of 1.5x
@author: Abhishek Koshta
"""

# Importing libraries to read data
import time
st = time.clock()
from nsetools import Nse
import pandas as pd
import time
from datetime import date
nse = Nse()

# Initializing an empty list for saving the stocks with the pattern matched
brk_list=[]
count=1 # Vaiable to get how many stocks have been screended while running the programme
# Reading the csv file for stock codes
all_stock_codes = pd.read_csv("all_stock_codes.csv")
#all_stock_codes = pd.read_csv("fno.csv")

# Starting a loop for going through stocks one by one
for stk in range(len(all_stock_codes)):
	stock =  all_stock_codes['0'][stk]
#	stock =  all_stock_codes['Code'][stk]    
	count+=1
	print (count,stock)  # Printing count and name of the stock for our convenience
	if stock == "SYMBOL" or stock=="COMPANY":
		continue
	try:
        # Reading the csv file downloaded from NSE of the stock 
		st_read = pd.read_csv("C:\\Python27\\Stock Market\\Working\\Stocks_NSE\\{}.csv".format(stock))
		check=0   # Putting check equals to zero, this will later on used for checking the conditions matched

	except:
		continue

    # Parameters to be changed
	days = len(st_read['High'])     # Counting the total number of days provided in the csv file
	atr_brk_v=1.5					# Coefficient for changing the volume break out condition
	atr_brk = 1.3					# Coefficient for changing the price break out condition
	eta_SMAP = 0.02					# Coefficient for altering the doji body length
	n = 5 							# Number of days for which doji has to be formed
    
	try:
		# Calculating the average true range for last n-1 days
		ATR = st_read['High'][::-1][:n][1:] - st_read['Low'][::-1][:n][1:]
		ATR = ATR.mean()
		# Calculating simple moving average price for last n-1 days
		SMAP = st_read['Last'][::-1][:n][1:].mean()
		# Calculating simple moving average volume for last n-1 days
		SMAV = st_read['Volume'][::-1][:n][1:].mean()
		# Defining upper and lower prices to check if a stock has broke out in up/down direction
		atr_break_u = st_read['Last'][days-2] + ATR*atr_brk
		atr_break_d = st_read['Last'][days-2] - ATR*atr_brk
	except:
		continue
	for i in range(1,4):			# Checking doji for last 3 days and then an ATR breakout
		if SMAP*(1+eta_SMAP) >= st_read['Last'][days-i]  and SMAP*(1-eta_SMAP) <= st_read['Last'][days-i] :
			check+=1; print ("Check",check)

		# Checking the ATR break out pattern along with doji has satisfied volume break out or not	
		if check == 3:
			print (stock)
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