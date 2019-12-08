import pandas as pd
from nsetools import Nse
import csv 
from datetime import date  
from pprint import pprint # just for neatness of display
nse = Nse()

all_stock_codes = pd.read_csv("all_stock_codes.csv")
for stk in range(len(all_stock_codes)):
	stock =  all_stock_codes['0'][stk]
	print (stock)
	try:
		q = nse.get_quote(stock) # it's ok to use both upper or lower case for codes.
	except:
		print ("Problematic Stock", stock)
		continue
	# pprint(q)
	# [Date	stock	Series	Prev Close	Open	High	Low	Last	Close	VWAP	Volume	
	# Turnover	Trades	Deliverable Volume	%Deliverble]\
		# fields = [date.today(),stock,'EQ',q['previousClose'], q['open'],q['dayHigh'],q['dayLow'],q['basePrice'],q['closePrice'],
		# 'VWAP', q['quantityTraded'],'Turnover','Trades', q['deliveryQuantity'], q['deliveryToTradedQuantity']]
	try:
		fields = [date.today(),stock,'EQ',q['previousClose'], q['open'],q['dayHigh'],q['dayLow'],'Last',q['closePrice'],
		'VWAP', 'quantityTraded','Turnover','Trades', 'deliveryQuantity', 'deliveryToTradedQuantity']
	except:
		print ("problem fetching data for", stock)
		continue

	addr = r"E:\\Abhishek\\Coding\\Stock Market\\Stocks_NSE\\{}.csv".format(stock)
	with open(addr, 'a') as f:
	    writer = csv.writer(f)
	    writer.writerow(fields)

