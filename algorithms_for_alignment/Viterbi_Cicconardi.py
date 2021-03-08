#define states and emission probabilities
T = {'Begin_Yes':0.2, 'Begin_No':0.8, 'Yes_to_No':0.2, 'No_to_Yes':0.1, 'Yes_to_Yes':0.7, 'No_to_No':0.8, 'End_Yes':0.1, 'End_No':0.1}
E = {'Yes_A': 0.1, 'Yes_C': 0.4, 'Yes_T': 0.1, 'Yes_G': 0.4, 'No_A': 0.25, 'No_C': 0.25, 'No_T': 0.25, 'No_G': 0.25}

#define sequence and states
seq = 'ATGCGCGC'
states = ['B', 'Y', 'N', 'E']

#create matrix and inizialize it
Matrix = [[0 for i in range(len(seq)+2)] for j in range(len(states))]

#define pretty matrix
def prettymatrix(M):
	for i in range(len(M)):
		print (M[i])
	return M

#define the population algorithm
def population_matrix(Matrix, seq):
	Matrix[0][0] = 1
	top = []
	bottom = []
	pathway = ''
	if seq[0] == 'A':
		Matrix[1][1] = ((1*T['Begin_Yes']*E['Yes_A']), 'End')
		Matrix[2][1] = ((1*T['Begin_No']*E['No_A']), 'End')
	elif seq[0] == 'T':
		Matrix[1][1] = ((1*T['Begin_Yes']*E['Yes_T']), 'End')
		Matrix[2][1] = ((1*T['Begin_No']*E['No_T']), 'End')
	elif seq[0] == 'C':
		Matrix[1][1] = ((1*T['Begin_Yes']*E['Yes_C']), 'End')
		Matrix[2][1] = ((1*T['Begin_No']*E['No_C']), 'End')
	else:
		Matrix[1][1] = ((1*T['Begin_Yes']*E['Yes_G']), 'End')
		Matrix[2][1] = ((1*T['Begin_No']*E['No_G']), 'End')

	for i in range(2, len(seq)+1):
		if seq[i-1] == 'A':
			top = [(Matrix[1][i-1][0]*T['Yes_to_Yes']*E['Yes_A']) , (Matrix[2][i-1][0]*T['No_to_Yes']*E['Yes_A'])]
			bottom = [(Matrix[1][i-1][0]*T['Yes_to_No']*E['No_A']) , (Matrix[2][i-1][0]*T['No_to_No']*E['No_A'])]
			if max(top) == (Matrix[1][i-1][0]*T['Yes_to_Yes']*E['Yes_A']):
				Matrix[1][i] = (max(top) , 'Y')
			else:
				Matrix[1][i] = (max(top) , 'N')
			if max(bottom) == (Matrix[1][i-1][0]*T['Yes_to_No']*E['No_A']):
				Matrix[2][i] = (max(bottom), 'Y')
			else:
				Matrix[2][i] = (max(bottom), 'N')

		elif seq[i-1] == 'T':
			top = [(Matrix[1][i-1][0]*T['Yes_to_Yes']*E['Yes_T']) , (Matrix[2][i-1][0]*T['No_to_Yes']*E['Yes_T'])]
			bottom = [(Matrix[1][i-1][0]*T['Yes_to_No']*E['No_T']) , (Matrix[2][i-1][0]*T['No_to_No']*E['No_T'])]
			if max(top) == (Matrix[1][i-1][0]*T['Yes_to_Yes']*E['Yes_T']):
				Matrix[1][i] = (max(top) , 'Y')
			else:
				Matrix[1][i] = (max(top) , 'N')
			if max(bottom) == (Matrix[1][i-1][0]*T['Yes_to_No']*E['No_T']):
				Matrix[2][i] = (max(bottom), 'Y')
			else:
				Matrix[2][i] = (max(bottom), 'N')

		elif seq[i-1] == 'C':
			top = [(Matrix[1][i-1][0]*T['Yes_to_Yes']*E['Yes_C']) , (Matrix[2][i-1][0]*T['No_to_Yes']*E['Yes_C'])]
			bottom = [(Matrix[1][i-1][0]*T['Yes_to_No']*E['No_C']) , (Matrix[2][i-1][0]*T['No_to_No']*E['No_C'])]
			if max(top) == (Matrix[1][i-1][0]*T['Yes_to_Yes']*E['Yes_C']):
				Matrix[1][i] = (max(top) , 'Y')
			else:
				Matrix[1][i] = (max(top) , 'N')
			if max(bottom) == (Matrix[1][i-1][0]*T['Yes_to_No']*E['No_C']):
				Matrix[2][i] = (max(bottom), 'Y')
			else:
				Matrix[2][i] = (max(bottom), 'N')

		else:
			top = [(Matrix[1][i-1][0]*T['Yes_to_Yes']*E['Yes_G']) , (Matrix[2][i-1][0]*T['No_to_Yes']*E['Yes_G'])]
			bottom = [(Matrix[1][i-1][0]*T['Yes_to_No']*E['No_G']) , (Matrix[2][i-1][0]*T['No_to_No']*E['No_G'])]
			if max(top) == (Matrix[1][i-1][0]*T['Yes_to_Yes']*E['Yes_G']):
				Matrix[1][i] = (max(top) , 'Y')
			else:
				Matrix[1][i] = (max(top) , 'N')
			if max(bottom) == (Matrix[1][i-1][0]*T['Yes_to_No']*E['No_G']):
				Matrix[2][i] = (max(bottom), 'Y')
			else:
				Matrix[2][i] = (max(bottom), 'N')

	j = len(seq)+1
	k = max(Matrix[1][j-1][0], Matrix[2][j-1][0])
	r = 0
	if k == Matrix[1][j-1][0]:
		Matrix[3][j] = (k*T['End_Yes'], 'Y')
	else:
		Matrix[3][j] = (k*T['End_No'], 'N')

	if Matrix[3][j][1] == 'Y':
		pathway += 'Y'
		r = 1
	else:
		pathway += 'N'
		r = 2
	j = j-1
	for i in range(j, 0, -1):
		if Matrix[r][i][1] == 'Y':
			pathway += 'Y'
			r = 1
		else:
			pathway += 'N'
			r = 2
	print ("The path is:", pathway [::-1])
	return (Matrix)


Riccardo_Benzoni = population_matrix(Matrix, seq)
prettymatrix (Riccardo_Benzoni)

