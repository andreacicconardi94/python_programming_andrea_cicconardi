#define the dictionary of Transition and Emission probabilities

T = {'Begin_yes':0.2, 'Begin_no':0.8, 'Yes_to_No':0.2, 'No_to_Yes':0.1, 'Yes_to_Yes':0.7, 'No_to_No':0.8, 'End_Yes':0.1, 'End_No':0.1}
E = {'Yes_A': 0.1, 'Yes_C': 0.4, 'Yes_T': 0.1, 'Yes_G': 0.4, 'No_A': 0.25, 'No_C': 0.25, 'No_T': 0.25, 'No_G': 0.25}


#define the sequence and the states
Seq = 'ATGCG'
States = ['B', 'Y', 'N', 'E']

#create the matrix and inizialize it
Matrix = [[0 for i in range(len(Seq)+2)] for j in range(len(States))]

#define pretty matrix
def prettymatrix(M):
	for i in range(len(M)):
		print(M[i])
	return M


def population_matrix(Matrix, Seq):
	Matrix[0][0] = 1
	if Seq[0] == 'A':
		Matrix[1][1] = 1*T['Begin_yes']*E['Yes_A']
		Matrix[2][1] = 1*T['Begin_no']*E['No_A']
	elif Seq[0] == 'T':
		Matrix[1][1] = 1*T['Begin_yes']*E['Yes_T']
		Matrix[2][1] = 1*T['Begin_no']*E['No_T']
	elif Seq[0] == 'C':
		Matrix[1][1] = 1*T['Begin_yes']*E['Yes_C']
		Matrix[2][1] = 1*T['Begin_no']*E['No_C']
	else:
		Matrix[1][1] = 1*T['Begin_yes']*E['Yes_T']
		Matrix[2][1] = 1*T['Begin_no']*E['No_T']
	
	for i in range(2, len(Seq)+1):
		if Seq[i-1] == 'A':
			Matrix[1][i] = (((Matrix[1][i-1]*T['Yes_to_Yes'])+(Matrix[2][i-1]*T['No_to_Yes']))*E['Yes_A'])
			Matrix[2][i] = (((Matrix[2][i-1]*T['No_to_No'])+(Matrix[1][i-1]*T['Yes_to_No']))*E['No_A'])
		elif Seq[i-1] == 'T':
			Matrix[1][i] = (((Matrix[1][i-1]*T['Yes_to_Yes'])+(Matrix[2][i-1]*T['No_to_Yes']))*E['Yes_T'])
			Matrix[2][i] = (((Matrix[2][i-1]*T['No_to_No'])+(Matrix[1][i-1]*T['Yes_to_No']))*E['No_T'])
		elif Seq[i-1] == 'C':
			Matrix[1][i] = (((Matrix[1][i-1]*T['Yes_to_Yes'])+(Matrix[2][i-1]*T['No_to_Yes']))*E['Yes_C'])
			Matrix[2][i] = (((Matrix[2][i-1]*T['No_to_No'])+(Matrix[1][i-1]*T['Yes_to_No']))*E['No_C'])
		else:
			Matrix[1][i] = (((Matrix[1][i-1]*T['Yes_to_Yes'])+(Matrix[2][i-1]*T['No_to_Yes']))*E['Yes_G'])
			Matrix[2][i] = (((Matrix[2][i-1]*T['No_to_No'])+(Matrix[1][i-1]*T['Yes_to_No']))*E['No_G'])
	j = len(Seq)+1
	Probability = 0
	Matrix[3][j] = ((Matrix[1][j-1]*T['End_Yes']) + (Matrix[2][j-1]*T['End_No']))
	Probability = Matrix[3][j]
	print ("The probability of this sequence is:", Probability)
	return Matrix

M = population_matrix(Matrix, Seq)
prettymatrix(M)
