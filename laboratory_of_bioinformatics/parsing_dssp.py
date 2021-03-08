#usr/bin/python

import sys
#Norm_Acc={"A" :106.0, "B" :160.0, "C" :135.0, "D" :163.0, "E" :194.0,"F" :197.0, "G" : 84.0, "H" :184.0,"I" :169.0, "K" :205.0, "L" :164.0,"M" :188.0, "N" :157.0, "P" :136.0,"Q" :198.0, "R" :248.0, "S" :130.0,"T" :142.0, "V" :142.0, "W" :227.0,"X" :180.0, "Y" :222.0, "Z" :196.0}


def parse_dssp(dsspfile, ch):
	c=0
	f=open(dsspfile)
	seq=''
	secstr=''
	for line in f:
		if line.find('#  RESIDUE')==2:	#if it match this it is the $2 of the line
			c=1
			continue
		if c==0:continue
		if line[13]=='!': continue
		if line[11]==ch:
			residue=line[13]
			ss=line[16]
			if ss==' ' or ss=='S' or ss=='T':
				ss='C'
			elif ss=='B' or ss=='E':
				ss='E'
			else:
				ss='H'
			acc=float(line[35:38])
			phi=float(line[103:109])
			psi=float(line[109:115])
			racc=min(acc/Norm_Acc[r], 1.0)
			seq+=residue
			secstr+=ss
	return seq , secstr





if __name__ == "__main__":
	dsspfile = sys.argv[1]
	ch = sys.argv[2]
	id = sys.argv[3]
	obj1 = parse_dssp(dsspfile,ch)
	print('%s_%s'	%(id,ch))
	print(obj1)
	#print(obj2)
