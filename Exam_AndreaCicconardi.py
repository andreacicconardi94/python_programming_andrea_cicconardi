seq1 = 'ACTGC'
seq2 = 'ACTTCG'
Match = +2
Mismatch1 = -1
Mismatch2 = -2
Gap = -3

row = len(seq1)+1
col = len(seq2)+1

score_matrix = [[0 for i in range(col)] for j in range(row)]
traceback_matrix = [['stop!' for i in range(col)] for j in range(row)]

def pretty_matrix(M):
	for i in M:
		print (i)
	return M

def population_matrix (score_matrix, traceback_matrix):
	scores = []
	trace = []
	for i in range (1, len(seq1)):
		for j in range(1, len(seq2)):
			up_score = score_matrix[i-1][j] + Gap
			left_score = score_matrix[i][j-1] + Gap
			if seq1[i-1] == seq2[j-1]:
				diag_score = score_matrix[i-1][j-1] + Match
			elif (seq1[i-1] == 'A' and seq2[j-1] == 'C') or (seq1[i-1] == 'C' and seq2[j-1] == 'A') or (seq1[i-1] == 'T' and seq2[j-1] == 'G') or (seq1[i-1] == 'G' and seq2[j-1] == 'T'):
				diag_score = score_matrix[i-1][j-1] + Mismatch1
			else:
				diag_score = score_matrix[i-1][j-1] + Mismatch2

			scores = [up_score, left_score, diag_score, 0]
			trace = ['up', 'left', 'diag', 'stop!']
			for k in range(len(scores)):
				if scores[k] == max(scores):
					score_matrix[i][j] = scores[k]
					traceback_matrix[i][j] = trace[k]

	pretty_matrix(score_matrix)
	pretty_matrix(traceback_matrix)
	return score_matrix, traceback_matrix

def alignment_function (score_matrix, traceback_matrix):
	I = 0
	J = 0
	alignment1 = ''
	alignment2 = ''
	start = 0
	for i in range(row):
		for j in range(col):
			if score_matrix[i][j] >= start:
				start = score_matrix[i][j]
				I = i
				J = j

	while traceback_matrix[I][J] != 'stop!':
		if traceback_matrix[I][J] == 'up':
			alignment1 += seq1[I-1]
			alignment2 += '-'
			I += -1
		elif traceback_matrix[I][J] == 'left':
			alignment2 += seq2[J-1]
			alignment1 += '-'
			J += -1
		else:
			alignment1 += seq1[I-1]
			alignment2 += seq2[J-1]
			I += -1
			J += -1

	print ("This is the best local alignment: ")
	print (alignment1 [::-1])
	print (alignment2 [::-1])
	return alignment1, alignment2

population_matrix(score_matrix, traceback_matrix)
alignment_function(score_matrix, traceback_matrix)
