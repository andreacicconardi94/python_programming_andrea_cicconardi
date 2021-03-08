import sys

file=sys.argv[1]					#It checks if the sequence and the secondary structure have same lenght

with open(file, 'r') as reader:
	i=reader.readlines()
	for j in range(1,len(i),3):			#The file is in format HEADER-SEQUENCE-SS so j=1 is the Sequence
		if len(i[j])==len(i[j+1]):		#If the sequence and the ss have same lenght it prints the entry
			print(i[j-1])
			print(i[j])
			print(i[j+1])

