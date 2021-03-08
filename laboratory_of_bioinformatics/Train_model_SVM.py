#Script that takes in input the list of ID, parse their profile and build a Model from their secondary structure

import numpy as np
from sklearn import svm
from sklearn.datasets import load_svmlight_file
import pickle, gzip
import sys

#mySVC = svm.SVC(C=2.0, kernel ='rbf', gamma=2.0)
#mySVC = svm.SVC(C=2.0, kernel='rbf', gamma=0.5)
mySVC = svm.SVC(C=4.0, kernel='rbf', gamma=2.0)
#mySVC = svm.SVC(C=4.0, kernel='rbf', gamma=0.5)

def parsing(file):                	     #Function that takes in input a pssm file, previous formatted in bash, and
	Filelines=file.readlines()                              #returns the matrix of the profile
        Matrix=[[] for i in range(len(Filelines))]              #Create an inizial empty matrix
        a=0
        for line in Filelines:
                l=line.split()
                if a==0:                        #The first line, that contains only letter of AA as string, is treated diff$
                        a+=1
                else:                           #It add the next line as numbers to normalize them in the matrix
                        for i in range(22,42):
                                I=float(l[i])
                                Matrix[a].append(I/100)
                        a+=1
        Matrix=Matrix[1:len(Matrix)]            #I cut the first empty row
        return Matrix



def SVM(Matrix, ss):
	Padding=[[0.0 for x in range(0,20)] for y in range(0,8)]
        Profile=Padding+Matrix+Padding
	SS=ss.readlines()[1].strip()
	Classes=[]
	Prof=[]
	for character in SS:
		if character=='H':
                	Class=1
                elif character=='E':
                        Class=2
                else:
                        Class=3

                Classes.append(Class)

	for i in range(0, len(SS)):
                W=Profile[i:i+17]
		tmp_profile=[]
		for j in range(0,17):
			for k in range(0,20):
				tmp_profile.append(W[j][k])

		Prof.append(tmp_profile)

	return Prof, Classes


if __name__=='__main__':
	#list=sys.argv[1]
	#list=open(list)
	#General_Prof=[]
	#General_Classes=[]
	#for i in list:
		#i=i.rstrip()
		#try:
		#	pssm=open(i+'_formatted.pssm')
		#	seq=open('formatted_'+i+'.dssp')
		#except:
		#	continue

		#m = parsing(pssm)
		#Profile, Classes = SVM(m, seq)
		#General_Prof.extend(Profile)
		#General_Classes.extend(Classes)

	#np_profile=np.array(General_Prof)
	#np.save("np_profile_4", np_profile)
	#np_classes=np.array(General_Classes)
	#np.save("np_classes_4", np_classes)

	Profile=np.load("np_profile_0.npy")
	Classes=np.load("np_classes_0.npy")
	mySVC = svm.SVC(C=4.0, kernel='rbf', gamma=2.0)
	mySVC.fit(Profile, Classes)
	pickle.dump(mySVC, gzip.open('Model_0_0.pkl.gz', 'w'))
