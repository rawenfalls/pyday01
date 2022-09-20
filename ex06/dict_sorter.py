#!/usr/local/bin/python3

import sys

def dict_sorter():
	list_of_tuples = [
		('Russia', '25'),
		('France', '132'),
		('Germany', '132'),
		('Spain', '178'),
		('Italy', '162'),
		('Portugal', '17'),
		('Finland', '3'),
		('Hungary', '2'),
		('The Netherlands', '28'),
		('The USA', '610'),
		('The United Kingdom', '95'),
		('China', '83'),
		('Iran', '76'),
		('Turkey', '65'),
		('Belgium', '34'),
		('Canada', '28'),
		('Switzerland', '26'),
		('Brazil', '25'),
		('Austria', '14'),
		('Israel', '12')
	]
	if len(sys.argv) == 1:
		contries = {}
		number = []
		for a, b in list_of_tuples:
			contries[int(b)] = []
			contries[int(b)].append(a)
			number.append(b)
		sort = list(reversed(sorted(contries)))

		print(sort)
	# for a in sort:
	# 	for key, value in contries.items():
	# 		for i in value:
	# 			if i == a[0]:
	# 				print("'" + str(key) + "' : '" + i + "'")


if __name__ == '__main__':
	dict_sorter()
