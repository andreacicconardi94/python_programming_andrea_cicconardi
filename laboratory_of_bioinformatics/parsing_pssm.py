#/opt/conda/bin/python

#Script to parse a formatted pssm file, that contains only the two matrices

import sys


def parsing(file):
	File=open(file)
	File1=open(file)
	Matrix=[[] for line in File1]		#Create an inizial empty matrix
	a=0
	for line in File:
		l=line.split()
		if a==0:			#The first line, that contains only letter of AA as string, is treated differently
			Matrix[0]=l[0:20]
			a+=1
		else:				#It add the next line as numbers to normalize them in the matrix
			for i in range(22,41):
				I=int(l[i])
				Matrix[a].append(I/100)
			a+=1
	for rows in Matrix:			#Print a pretty Matrix
		print(rows)



if __name__ == "__main__":
	F1=sys.argv[1]
	parsing(F1)
