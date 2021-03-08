#Script that takes in input the list of ID to predict their secondary structure using a particular model

import numpy as np
from sklearn import svm
import pickle, gzip
import sys


if __name__=='__main__':
	test=sys.argv[1]
	list=open(test)
	for i in range(1,
		Profiles
	for i in list:
		i=i.rstrip()
		try:
			pssm=open(i+'_formatted.pssm')
		except:
			continue
		Profile_line=pssm.readlines()
		for p_line in Profile_line:
			counter_zero=0
			tmp_profile=[]
			l=p_line.split()
			for i in range(22,42):
				try:
					I=float(l[i])
					counter_zero+=I
				except:
					continue

				if counter_zero!=0:
					tmp_profile.append(I/100)
				else:
					continue
			Profiles.append(tmp_profile)


	mySVC = open('svm_model_4_C4.0_G2.0.dump', 'r')
	Prediction = mySVC.predict(Profiles)
	pickle.dump(Prediction ('prediction_4_C4.0_G2.0.dump', 'w'))
