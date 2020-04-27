#!/usr/bin/python

def conversion(num):
	dec_num=int(str(num),2)
	oct_num=format(dec_num,'o')
	hex_num=format(dec_num,'X')
	return("=> OCT> %s \n=> DEC> %s \n=> HEX> %s" %(oct_num, dec_num, hex_num))

if __name__=='__main__':
	print("no input")
