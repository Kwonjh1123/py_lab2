#!/usr/bin/python
import re

def uni_inter(a,b):
	num_1=re.findall('\[(.*?)\]', a)
	num_2=re.findall('\[(.*?)\]', b)
	fir=num_1[0].replace(" ","")
	sec=num_2[0].replace(" ","")
	fst_list=fir.split(",")
	snd_list=sec.split(",")
	union=(','.join([str(i) for i in sorted(list(set(fst_list)|set(snd_list)))]))
	inter=(','.join([str(i) for i in sorted(list(set(fst_list)&set(snd_list)))]))
	return("=> union [%s] \n=> intersection [%s]" %(union, inter))

if __name__=='__main__':
	print("no input")
