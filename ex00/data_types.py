#!/usr/local/bin/python3

import string

def data_types():
	variables = (
		1,							#int
		'string',					#str
		4.2,						#dloat
		True,						#boll
		[1, 2, 3, '100'],			#list
		{'first': 1, 'second': 2},	#map
		(1, 'asd', True), 			#tupe
		{1,4,3,5,2}					#set
	)
	
	out_string = '['
	for var in variables:
		out_string += type(var).__name__ + ', '
	out_string = out_string[:-2] + ']'
	print (out_string)



if __name__ == '__main__':
	data_types()
