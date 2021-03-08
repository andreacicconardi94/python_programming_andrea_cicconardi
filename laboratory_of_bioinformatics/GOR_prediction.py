import sys
import numpy as np
import math
import re

def parsing(file):			                     #Function that takes in input a pssm file, previous formatted in bash, and
	Filelines=file.readlines()                           #returns the matrix of the profile
	Matrix=[[] for i in range(len(Filelines))]           #Create an inizial empty matrix
	a=0
	for line in Filelines:
		l=line.split()
		if a==0:                        #The first line, that contains only letter of AA as string, is treated differently
			a+=1
		else:                           #It add the next line as numbers to normalize them in the matrix
			for i in range(22,42):
				I=int(l[i])
				Matrix[a].append(I/100)
			a+=1
	Matrix=Matrix[1:len(Matrix)]            #I cut the first empty row
	return Matrix




def Prediction(matrix, dssp):						#Function to predict secondary structure
	Helix=np.load("Matrix_Helix_Train.npy")				#First it opens the matrix from the train
	Coil=np.load("Matrix_Coil_Train.npy")
	Strand=np.load("Matrix_Strand_Train.npy")
	Residue=np.load("Matrix_Residue_Train.npy")
	Sec_Str=np.load("Matrix_SS_Train.npy")
	I_H=0.0								#it inizializes the counters for Information Function
	I_C=0.0
	I_S=0.0
	Predicted_structure=""						#it inizializes the empty string for the ss
	Padding=[[0.0 for x in range(0,20)] for y in range(0,8)]
	SS=dssp								#I create Padding matrix to avoid the empty line problem in
	ss=SS.readlines()[2].strip()					#Reads only the Secondary Structure line
	Profile=Padding+matrix+Padding					#Inizialize the matrix with paddings
	for i in range(0, len(ss)):
		W=Profile[i:i+17]					#This is the window
		for j in range(0,17):
			for k in range(0,20):
				I_H+=(math.log((Helix[j][k])/(Sec_Str[2]*Residue[j][k]))*W[j][k])	#compute the information
				I_S+=(math.log((Strand[j][k])/(Sec_Str[1]*Residue[j][k]))*W[j][k])	#function for each ss
				I_C+=(math.log((Coil[j][k])/(Sec_Str[0]*Residue[j][k]))*W[j][k])
		SS_predicted=max(I_H, I_S, I_C)								#choose the max among them
		if SS_predicted==I_H:
			Predicted_structure=Predicted_structure + "H"				 #add a characted to the ss string
		elif SS_predicted==I_S:
			Predicted_structure=Predicted_structure + "E"
		else:
			Predicted_structure=Predicted_structure + "C"

		I_H=0.0
		I_S=0.0
		I_C=0.0
	print ("The predicted sequence is:\n%r" %Predicted_structure)
	print ("The observed sequence is:\n%r" %ss)
	return Predicted_structure, ss


def evaluation(confusion_matrix, fasta_file, pred_structure):		#Function that computes the confusion matrix to evaluate GOR
	SEC_STR=fasta_file						#It takes in input the observed secondary structure and the
	sec_str=SEC_STR.readlines()[2].strip()				#predicted one. Then it compares them to populate the matrix
	for i in range(0, len(sec_str)):
		if pred_structure[i]=="H":
			if pred_structure[i]==sec_str[i]:
				confusion_matrix[0][0]+=1
			elif sec_str[i]=="E":
				confusion_matrix[0][1]+=1
			else:
				confusion_matrix[0][2]+=1

		elif pred_structure[i]=="E":
			if pred_structure[i]==sec_str[i]:
				confusion_matrix[1][1]+=1
			elif sec_str[i]=="H":
				confusion_matrix[1][0]+=1
			else:
				confusion_matrix[1][2]+=1

		else:
			if pred_structure[i]==sec_str[i]:
				confusion_matrix[2][2]+=1
			elif sec_str[i]=="H":
				confusion_matrix[2][0]+=1
			else:
				confusion_matrix[2][1]+=1

	return confusion_matrix


def SOV(predicted, observed):
	sequences = [predicted, observed]
	fragments = {'H':[[],[]], 'E':[[], []], 'C':[[], []]}
	alphabet_of_ss = ['H', 'E', 'C']
	minov=[]
	maxov=[]
	delta=[]
	lenghts=[]
	SOV=[]
	for character in alphabet_of_ss:
		search_segment = re.escape(character) + r"+"		#it search in the sequence if there is a substring that
		for sequence, number in zip(sequences, range(0,2)):	#contains only selected character and divide it with a '+'
			count1 = 0
			while character in sequence[count1:]:
				sequence_remain = sequence[count1:]
				single_fragment = []
				x = re.search(search_segment,sequence_remain)	#search segment in the overall sequence
				for i in range(x.span()[0]+count1, x.span()[1]+count1):	#i is from the begin index and the ending index
					single_fragment.append(i)		#it appends the index of the selected residue in the fragment
				fragments[character][number].append(sorted(single_fragment))	#append the indexes of the segment in
				count1 += x.span()[1]						#the dictionary of fragments


	for sec_str, frag in fragments.items():
		N_res=0.0
		tmp_SOV=0.0
		for a in frag[0]:
			for b in frag[1]:
				tmp_minov = set(a) & set(b)
				tmp_maxov = set(a) | set(b)
				tmp_delta = max((len(tmp_maxov)-len(tmp_minov)), len(tmp_minov), len(a)/2, len(b)/2)
				N_res += len(b)
				if len(tmp_minov)>0:
					minov.append(len(tmp_minov))
					maxov.append(len(tmp_maxov))
					delta.append(tmp_delta)
					lenghts.append(len(b))
		for c in range(0, len(minov)):
			tmp_SOV += ((minov[c]+delta[c])/maxov[c] * lenghts[c])
		tmp_SOV = (100/N_res)*(tmp_SOV)
		SOV.append(tmp_SOV)

	return SOV











if __name__=='__main__':
	list=sys.argv[1]
	list=open(list)
	counter=0
	S=[0,0,0]
	CM=[[0.0 for i in range(0,3)] for j in range(0,3)]
	for i in list:
		if counter<=150:
			i=i.rstrip()
			try:
				pssm=open(i+'_formatted.pssm')
				fasta=open(i+'.fasta')
				fasta2=open(i+'.fasta')
			except:
				continue
			M=parsing(pssm)
			PS, OS=Prediction(M, fasta)
			CM=evaluation(CM, fasta2, PS)
			tmp_S = SOV(PS, OS)
			for k in range(0, len(tmp_S)):
				S[k] += tmp_S[k]
			counter+=1

	print ('Final SOV_H is:\n{0}\n, Final SOV_E is:\n{1}\n, Final SOV_C is: \n{2}'.format(S[0]/counter, S[1]/counter, S[2]/counter))

	C_H=(CM[0][0])								#True positive for H
	O_H=(CM[0][1]+CM[0][2])							#False positive for H
	U_H=(CM[1][0]+CM[2][0])							#False negative for H
	N_H=(CM[1][1]+CM[1][2]+CM[2][1]+CM[2][2])				#True negative for H

	C_E=(CM[1][1])								#True positive for E
	O_E=(CM[1][0]+CM[1][2])							#False positive for E
	U_E=(CM[0][1]+CM[2][1])							#False negative for E
	N_E=(CM[0][0]+CM[0][2]+CM[2][0]+CM[2][2])				#True negative for E

	C_C=(CM[2][2])								#True positive for C
	O_C=(CM[2][0]+CM[2][1])							#False positive for C
	U_C=(CM[0][2]+CM[1][2])							#False negative for C
	N_C=(CM[0][0]+CM[0][1]+CM[1][0]+CM[1][1])				#True negative for C


	SEN_H= C_H/(C_H+U_H)							#Sensitivity for H
	PPV_H= C_H/(C_H+O_H)							#Positive Predictive Value
	MMC_H= ((C_H*N_H)-(O_H*U_H))/(math.sqrt((C_H+O_H)*(C_H+U_H)*(N_H+O_H)*(N_H+U_H)))


	SEN_E= C_E/(C_E+U_E)
	PPV_E= C_E/(C_E+O_E)
	MMC_E= ((C_E*N_E)-(O_E*U_E))/(math.sqrt((C_E+O_E)*(C_E+U_E)*(N_E+O_E)*(N_E+U_E)))

	SEN_C= C_C/(C_C+U_C)
	PPV_C= C_C/(C_C+O_C)
	MMC_C= ((C_C*N_C)-(O_C*U_C))/(math.sqrt((C_C+O_C)*(C_C+U_C)*(N_C+O_C)*(N_C+U_C)))

	Q_3= (C_H+C_E+C_C)/(C_H+O_H+U_H+N_H)					#Three-class accuracy

	print ("Three-class accuracy:\n%r" %Q_3)
	print ("Sensitivity for H is: {0}, for E is: {1}, for C is: {2}".format(SEN_H, SEN_E, SEN_C))
	print ("Positive Predictive Value for H is: {0}, for E is: {1}, for C is: {2}".format(PPV_H, PPV_E, PPV_C))
	print ("Matthew Correlation Coefficient for H is: {0}, for E is: {1}, for C is: {2}".format(MMC_H, MMC_E, MMC_C))
