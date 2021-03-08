#!/usr/bin/python3
import sys

import numpy as np

def conf_mat(filename, th, sp=-2, cp=-1):
	cm=[[0.0,0.0],[0.0,0.0]]
	f=open(filename)
	for line in f:
		v=line.rstrip().split()
		if int(v[cp])==1: i=1
		if int(v[cp])==0: i=0
		if float(v[sp])<th:
			j=1
		else:
			j=0
		cm[i][j]=cm[i][j]+1
		#print (cm)
		#raw_input("continue")
	return cm

def print_performance(cm):
	acc=(cm[0][0]+cm[1][1])/(cm[0][0]+cm[1][1]+cm[0][1]+cm[1][0])
	d=np.sqrt((cm[1][1]+cm[0][1])*(cm[1][1]+cm[1][0])*(cm[0][0]+cm[1][0])*(cm[0][0]+cm[0][1]))
	mc=(cm[1][1]*cm[0][0]-cm[0][1]*cm[1][0])/d
	TPR=(cm[1][1]/(cm[1][1]+cm[1][0]))
	FPR=(cm[0][1]/(cm[0][1]+cm[0][0]))
	print ('MAT=', cm, 'Q2', acc, 'MCC=', mc)
	print (TPR, FPR)



if __name__ == '__main__':
	filename=sys.argv[1]
	th=float(sys.argv[2])
	cm=conf_mat(filename,th)
	print (cm)
	#for i in cm:
	#	print (i)
	print_performance(cm)
