#!/usr/local/bin/python3

from curses.ascii import NUL


def read_and_write():
	f_r = open('ds.csv', 'r')
	f_w = open('ds.tsv', 'w')
	while (1):
		a = f_r.read(1)
		if not a:
			break
		if a != ",":
			f_w.write(a)
		else:
			f_w.write("\t")
	f_r.close()
	f_w.close()

if __name__ == '__main__':
	read_and_write()
