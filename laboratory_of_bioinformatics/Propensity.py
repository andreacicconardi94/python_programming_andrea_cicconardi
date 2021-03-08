#!/usr/bin/python
#calculate the propensity of each residue for Helix (H), Strand (E), and Coil (C)
#The propensity is defined as the inclination (or likelihood) of a residue to be in a certain conformation, for example Helix

import sys

#this function takes in input the sequence and the secondary structure of a protein and align them
def count_ss(filename):
	d_seq={}
	d_ss={}
	d_pair={}
	f=open(filename)
	for line in f:
		v=line.rstrip().split()
		n=len(v[0])
		for i in range(n):
			d_seq[v[0][i]]=d_seq.get(v[0][i],0)+1
			d_seq[v[1][i]]=d_ss.get(v[1][i],0)+1
			k=(v[0][i],v[1][i])
			d_pair[k]=d_pair.get(k,0)+1
	return d_seq,d_ss,d_pair


#from the alignment this function compute the propensity
def propensity(d_pair, d_seq, d_ss):
	ks=d_pair.keys()
	tot=float(sum(d_pair.values()))
	for k in ks:
		if k[1]==ss:
			prop=(d_pair[k]/tot)/((d_seq[k[0]]/tot)*(d_ss[k[1]]/tot))
			print (k, prop)


if __name__ == '__main__':
	d_seq,d_ss,d_pair=count_ss(sys.argv[1])
	propensity(d_pair, d_seq, d_ss,'H')
	propensity(d_pair, d_seq, d_ss,'E')
	propensity(d_pair, d_seq, d_ss,'C')
	print (d_seq, d_ss, d_pair,)
	print (sum(d_seq.values()), sum(d_ss.values())), sum(d_pair.values())
