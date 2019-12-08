import time
st = time.clock()
import pandas as pd
import time

#stock = "RELIANCE"
all_stock_codes = pd.read_csv("fno.csv")
for stk in range(len(all_stock_codes)):
	stock =  all_stock_codes['Code'][stk]
	st_read = pd.read_csv("C:\\Python27\\Stock Market\\Working\\FO_Stocks_NSE_10_yr_data\\{}.csv".format(stock))

	# Parameters to be changed
	days = len(st_read['High'])     # Counting the total number of days provided in the csv file
	atr_brk_v=2					# Coefficient for changing the volume break out condition
	atr_brk = 2					# Coefficient for changing the price break out condition
	eta_SMAP = 0.01					# Coefficient for altering the doji body length
	n = 5 							# Number of days for which doji has to be formed
	brk_list = []
	right = 0
	wrong = 0
	for j in range(days):
		check =0
		try:
			# Calculating the average true range for last n-1 days
			ATR = st_read['High'][j:j+3] - st_read['Low'][j:j+3]
			ATR = ATR.mean()
			# Calculating simple moving average price for last n-1 days
			SMAP = st_read['Close'][j:j+3].mean()
			# Calculating simple moving average volume for last n-1 days
			SMAV = st_read['Volume'][j:j+3].mean()
			# Defining upper and lower prices to check if a stock has broke out in up/down direction
			atr_break_u = st_read['Close'][j+3] + ATR*atr_brk
			atr_break_d = st_read['Close'][j+3] - ATR*atr_brk
	#		print ("breaking here")
		except:
		    pass
		for i in range(1,6):			# Checking doji for last 3 days and then an ATR breakout
			if (j+i-1) >= days:   break
			if SMAP*(1+eta_SMAP) >= st_read['Last'][j+i]  and SMAP*(1-eta_SMAP) <= st_read['Last'][j+i] :
				check+=1; #print ("Check",check)

			# Checking the ATR break out pattern along with doji has satisfied volume break out or not	
			if check == 3:
				if st_read['Last'][days-1] > atr_break_u:
					if st_read['Volume'][days-1] > SMAV*atr_brk_v:
						brk_list.append((stock,st_read["Last"][j+i],"Up",st_read["Date"][j+i]))
						# print ("=================Buy this stock=============",stock,st_read["Date"][j+i] )
						# print (stock,st_read["Last"][j+i],"Up",st_read["Last"][j+i+1])
						if st_read["Last"][j+i+1] >= st_read["Last"][j+i]:
							right+=1
							# print ("profit")
						else:
							wrong+=1					# time.sleep(2)

				if st_read['Last'][days-1] < atr_break_d:
					if st_read['Volume'][days-1] > SMAV*atr_brk_v:
						brk_list.append((stock,st_read["Last"][j+i],"Down",st_read["Date"][j+i]))
						# print ("=================Sell this stock=============",stock,st_read["Date"][j+i])
						# print (stock,st_read["Last"][j+i],"Down",st_read["Last"][j+i+1])
						if st_read["Last"][j+i+1] <= st_read["Last"][j+i]:
							right+=1
						else:
							wrong+=1

						# time.sleep(2)                    
	try:
		accuracy = right/(right+wrong)*100
		print ("===================Strategy is",round(accuracy,1),"% acuurate for", stock,"============================")
	except:
		continue
	sbrk_list = set(brk_list)
#print (set(brk_list), len(brk_list))
