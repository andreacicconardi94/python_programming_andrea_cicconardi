######################
## define the sequence
seq1 = "ACTGG"
seq2 = "ACCA"

print ("The two sequences are:")
print (seq1, '\n', seq2)

###############
##pretty matrix
def prettymatrix(M):
	for i in range(len(M)):
		print(M[i])
	return M

###############
##create matrix
def scoring_matrix(seq1, seq2):
	row = len(seq1)+1 
	col = len(seq2)+1
	Scoring = []
	for i in range(row):
		Scoring.append([])
		for j in range(col):
			Scoring[i].append(0)
	return Scoring

def traceback_matrix(seq1, seq2):
	row = len(seq1)+1 
	col = len(seq2)+1
	Traceback = []
	for i in range(row):
		Traceback.append([])
		for j in range(col):
			Traceback[i].append('stop!')
	return Traceback

Scoring = scoring_matrix(seq1, seq2)
Traceback = traceback_matrix(seq1, seq2)

##define funtion that populate matrix
def population_matrix (seq1, seq2, Scoring, Traceback):
	match = 2
	mismatch = -1
	gap = -2
	row = len(seq1)+1 
	col = len(seq2)+1
	scores = []
	path = []
	for i in range(1, col):
		for j in range(1, row):
			Score_Up = Scoring[j-1][i] + gap
			Score_Left = Scoring[j][i-1] + gap
			if seq2[i-1] == seq1[j-1]:
				Score_Diag = Scoring[j-1][i-1] + match
			else:
				Score_Diag = Scoring[j-1][i-1] + mismatch
			scores = [Score_Up, Score_Left, Score_Diag, 0]
			path = ['up', 'left', 'diag', 'stop!']
			Scoring[j][i] = max(scores)
			for k in range(len(scores)):
				if scores[k] == max(scores):
					Traceback[j][i] = path[k]
	return Scoring, Traceback



def alignment_function (Scoring, Traceback, seq1, seq2):
	row = len(seq1)+1
	col = len(seq2)+1
	I = 0
	J = 0
	alignment1 = ''
	alignment2 = ''
	Start = 0
	for i in range(col):
		for j in range(row):
			if Scoring[j][i] >= Start:
				Start = Scoring[j][i]
				I = i
				J = j
	while Traceback[J][I] != 'stop!':
		if Traceback[J][I] == 'up':
			alignment1 = alignment1 + '-'
			alignment2 = alignment2 + seq2[J-1]
			J = J-1
		elif Traceback[J][I] == 'left':
			alignment2 = alignment2 + '-'
			alignment1 = alignment1 + seq1[I-1]
			I = I-1
		elif Traceback[J][I] == 'diag':
			alignment1 = alignment1 + seq1[I-1]
			alignment2 = alignment2 + seq2[J-1]
			I = I-1
			J = J-1
	print ("Are you satisfied of this alignment?")
	print (alignment1[::-1])
	print (alignment2[::-1])
	return alignment1, alignment2

if __name__=='__main__':
	population_matrix (seq1, seq2, Scoring, Traceback)
	prettymatrix (Scoring)
	prettymatrix (Traceback)
	alignment_function (Scoring, Traceback, seq1, seq2)

