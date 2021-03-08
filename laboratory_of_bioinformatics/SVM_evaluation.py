#Script that takes in input the predicted sequence from SVM and returns the evaluation with a confusion matrix
#And with the SOV values

import sys
import numpy as np
import math
import re


def evaluation(confusion_matrix, fasta_file, pred_structure):		#Function that computes the confusion matrix to evaluate GOR
	SEC_STR=fasta_file						#It takes in input the observed secondary structure and the
	sec_str=SEC_STR.readlines()[2].strip()				#predicted one. Then it compares them to populate the matrix
	#pred_structure=Pred_structure.readlines()[2]
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
			try:
				tmp_SOV += ((minov[c]+delta[c])/maxov[c] * lenghts[c])
				tmp_SOV = (100/N_res)*(tmp_SOV)
				SOV.append(tmp_SOV)
			except:
				continue
	return SOV



if __name__=='__main__':
	list=sys.argv[1]
	list=open(list)
	ps=sys.argv[2]
	ps=open(ps)
	ps=ps.readlines()
	counter=[0,0,0]
	S=[0,0,0]
	CM=[[0.0 for i in range(0,3)] for j in range(0,3)]
	for i in list:
		i=i.rstrip()
		I='>'+i
		for j in range(0, len(ps)):
			ps[j]=ps[j].rstrip()
			if I==ps[j]:
				PS=ps[j+2]
				try:
					fasta=open(i+'_form.fasta')
					fasta2=open(i+'_form.fasta')
					OS=fasta2.readlines()[2].strip()
				except:
					continue

				CM=evaluation(CM, fasta, PS)
				tmp_S = SOV(PS, OS)
				for k in range(0, len(tmp_S)):
					try:
						S[k] += tmp_S[k]
						counter[k] += 1
					except:
						continue
			else:
				continue

	print ('Final SOV_H is:\n{0}\n, Final SOV_E is:\n{1}\n, Final SOV_C is: \n{2}'.format(S[0]/counter[0], S[1]/counter[1], S[2]/counter[2]))

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


	SEN_H = C_H/(C_H+U_H)							#Sensitivity for H
	PPV_H = C_H/(C_H+O_H)							#Positive Predictive Value
	MMC_H = ((C_H*N_H)-(O_H*U_H))/(math.sqrt((C_H+O_H)*(C_H+U_H)*(N_H+O_H)*(N_H+U_H)))


	SEN_E = C_E/(C_E+U_E)
	PPV_E = C_E/(C_E+O_E)
	MMC_E = ((C_E*N_E)-(O_E*U_E))/(math.sqrt((C_E+O_E)*(C_E+U_E)*(N_E+O_E)*(N_E+U_E)))

	SEN_C = C_C/(C_C+U_C)
	PPV_C = C_C/(C_C+O_C)
	MMC_C = ((C_C*N_C)-(O_C*U_C))/(math.sqrt((C_C+O_C)*(C_C+U_C)*(N_C+O_C)*(N_C+U_C)))

	Q_3 = (C_H+C_E+C_C)/(C_H+O_H+U_H+N_H)					#Three-class accuracy

	print ("Three-class accuracy:\n%r" %Q_3)
	print ("Sensitivity for H is: {0}, for E is: {1}, for C is: {2}".format(SEN_H, SEN_E, SEN_C))
	print ("Positive Predictive Value for H is: {0}, for E is: {1}, for C is: {2}".format(PPV_H, PPV_E, PPV_C))
	print ("Matthew Correlation Coefficient for H is: {0}, for E is: {1}, for C is: {2}".format(MMC_H, MMC_E, MMC_C))
