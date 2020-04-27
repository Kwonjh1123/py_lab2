#!/usr/bin/python

import my_pkg

if __name__== '__main__':

	a=0

	while 1 :

		a=input("Select menu: 1)conversion 2)union/intersection 3)exit ? ")
		if a=='1' :
			b=input("input binary number : ")
			print(my_pkg.conversion(b))
		elif a=='2' :
			c=input("1st list: ")
			d=input("2nd list: ")
			print(my_pkg.uni_inter(c,d))
		elif a=='3' :
			print("exit the program...")
			exit(0)		
		else :
			print("input wrong number")

