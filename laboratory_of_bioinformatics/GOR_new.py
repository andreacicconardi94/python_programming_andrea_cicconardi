#/opt/conda/bin/python

import sys
import numpy as np


def parsing(file, counter):			#Function that takes in input a pssm file, previous formatted in bash, and
	Filelines=file.readlines()				#returns the matrix of the profile
	Matrix=[[] for i in range(len(Filelines))]		#Create an inizial empty matrix
	a=0
	for line in Filelines:
		l=line.split()
		if a==0:			#The first line, that contains only letter of AA as string, is treated differently
			a+=1
		else:				#It add the next line as numbers to normalize them in the matrix
			for i in range(22,42):
				I=int(l[i])
				Matrix[a].append(I/100)
			a+=1
	Matrix=Matrix[1:len(Matrix)]		#I cut the first empty row
	counter+=1				#I need this counter later for all the file
	return Matrix, counter




def GOR(matrix, dssp, Res, SS_count):						#GOR algorithm to extract propensities of residue in SS
	Padding=[[0.0 for x in range(0,20)] for y in range(0,8)]	#Looking also at the context
	SS=dssp							#I create Padding matrix to avoid the empty line problem in
	Coil=[[0.0 for a in range(0,20)] for b in range(0,17)]		#The beginning and in the ending of the sequence
	Helix=[[0.0 for c in range(0,20)] for d in range(0,17)]
	Strand=[[0.0 for e in range(0,20)] for f in range(0,17)]
	Residue=[[0.0 for g in range(0,20)] for h in range(0,17)]
	Sec_Structure=[0.0 for z in range(0,3)]
	ss=SS.readlines()[1].strip()					#Reads only the Secondary Structure line
	Profile=Padding+matrix+Padding					#Inizialize the matrix with paddings
	for i in range(0, len(ss)):
		W=Profile[i:i+17]					#This is the window
		for j in range(0,17):
			for k in range(0,20):
				Res+=W[j][k]				#This counter increase by 1 for each residue whose profile is
				if ss[i]=='C':				#Different from 0
					Coil[j][k]+=W[j][k]
					Residue[j][k]+=W[j][k]
					Sec_Structure[0]+=1		#Sec_Structure[0] are the Coil
					SS_count+=1
				elif ss[i]=='E':			#Sec_Structure[1] are the Strand
					Strand[j][k]+=W[j][k]
					Residue[j][k]+=W[j][k]
					Sec_Structure[1]+=1
					SS_count+=1
				else:					#Sec_Structure[2] are the Helix
					Helix[j][k]+=W[j][k]
					Residue[j][k]+=W[j][k]
					Sec_Structure[2]+=1
					SS_count+=1
	return Coil, Strand, Helix, Residue, Res, SS_count, Sec_Structure	#At the end the function returns 4 matrices and the counter

def Normalization(FC,FS,FH,FR,R, Sec_Str, SS):				#This function normalize the 4 matrices dividing each element
	for i in range(0,17):						#For the number of residue
		for j in range(0,20):
			FC[i][j]=(FC[i][j]/R)
			FS[i][j]=(FS[i][j]/R)
			FH[i][j]=(FH[i][j]/R)
			FR[i][j]=(FR[i][j]/R)
		for k in range(0,3):
			Sec_Str[k]=(Sec_Str[k]/SS)
	return FC,FS,FH,FR,Sec_Str					#And returns all the matrices normalized


if __name__=='__main__':						#Here I slide all the file and sum all the matrices for each
	list=sys.argv[1]						#Of them to 4 matrices containing the total probabilities
	list=open(list)
	Final_Coil=[[0.0 for a in range(0,20)] for b in range(0,17)]    #Here I inizialize the 4 final matrices
	Final_Helix=[[0.0 for c in range(0,20)] for d in range(0,17)]
	Final_Strand=[[0.0 for e in range(0,20)] for f in range(0,17)]
	Final_Residue=[[0.0 for g in range(0,20)] for h in range(0,17)]
	Final_Sec_structure=[0.0 for z in range(0,3)]
	count=0
	ss=0.0
	R=0.0
	for i in list:
		i=i.rstrip()
		try:
			pssm=open(i+'_formatted.pssm')
			seq=open('formatted_'+i+'.dssp')
		except:
			continue
		m, count = parsing(pssm, count)
		Coil, Strand, Helix, Residue, R, ss, Sec_structure = GOR(m,seq,R,ss)
		for j in range(0,17):
			for k in range(0,20):				#And sum everytime the results to the final matrices
				Final_Coil[j][k]+=Coil[j][k]
				Final_Strand[j][k]+=Strand[j][k]
				Final_Helix[j][k]+=Helix[j][k]
				Final_Residue[j][k]+=Residue[j][k]
			for Y in range(0,3):
				Final_Sec_structure[Y]+=Sec_structure[Y]

	Final_Coil, Final_Strand, Final_Helix, Final_Residue, Final_Sec_structure = Normalization(Final_Coil,Final_Strand,Final_Helix,Final_Residue, R, Final_Sec_structure, ss)
	print("Coil probability matrix:\n%r" %Final_Coil) 			#Normalize them
	print("Strand probability matrix:\n%r" %Final_Strand)
	print("Helix probability matrix:\n%r" %Final_Helix)
	print("Residue probability matrix:\n%r" %Final_Residue)
	print("Secondary Structure probability matrix:\n%r" %Final_Sec_structure)
