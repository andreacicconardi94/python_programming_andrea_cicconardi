#Script to format the sequence as >ID in the first line, Fasta Sequence in the second, and Secondary Structure
#In the third line

import sys

def formatting(fasta, dssp, fasta1):

	Fasta=fasta.read().splitlines()[1]
	Dssp=dssp.read().splitlines()[1]
	ID=fasta1.read().splitlines()[0]
	final_file=ID+'\n'+Fasta+'\n'+Dssp+'\n'


	return final_file


if __name__=='__main__':
	list=sys.argv[1]
	list=open(list)
	list=list.read().splitlines()
	for i in list:
		try:
			outfile=open(i+'_form.fasta', 'w')
			fasta=open(i+'.fasta')
			fasta1=open(i+'.fasta')
			dssp=open('formatted_'+i+'.dssp')
			fin_file=formatting(fasta,dssp,fasta1)
			outfile.write(fin_file)
			outfile.close()
		except:
			continue
