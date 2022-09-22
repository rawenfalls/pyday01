#!/usr/local/bin/python3

import sys

def all_stocks():
	COMPANIES = {
		'Apple': 'AAPL',
		'Microsoft': 'MSFT',
		'Netflix': 'NFLX',
		'Tesla': 'TSLA',
		'Nokia': 'NOK'
	}
	STOCKS = {
		'AAPL': 287.73,
		'MSFT': 173.79,
		'NFLX': 416.90,
		'TSLA': 724.88,
		'NOK': 3.37
	}
	# print(len(sys.argv))

	if len(sys.argv) == 2:
		a = sys.argv[1].replace(" ", "").split(',')
		for var in a:
			var1 = var.capitalize()
			if var1 in COMPANIES:
				print(var1 + "stock price is " + str(STOCKS[COMPANIES[var1]]))
			elif var.upper() in COMPANIES.values():
				var1 = var.upper()
				for key, value in COMPANIES.items():
					if value == var1:
						print(var1 + " is a ticker symbol for " + key)
			else:
				print(var + " is an unknown company or an unknown ticker symbol")

if __name__ == '__main__':
	all_stocks()
