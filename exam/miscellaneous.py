# miscellaneous.py
'''
Exercise 1
'''
List=[21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39]
for i in List:
	if (i%2)==0:
		print (i)

for j in List:
	if (j%3)==0:
		print (j)

'''
Exercise 2
'''
print (List[-1],List[-2])

'''
Exercise 3
'''
L = [1,2,3]
for i in range(10):
	if i in L:
		print("i is in the list")
	else:
		print("i not found")    

 
'''
Exercise 4
'''
with open("sprot_prot.fasta") as Read:
	first_line = Read.readline().split("OS=")
	print (first_line[1])

'''
Exercise 5
'''
second_element = first_line[1].split(" ")
Second_element = second_element[0] + second_element[1]

'''
Exercise 6
'''

s= "asor rosa"
s[::-1]

'''
Exercise 7
'''
L=[1,7,3,9]
L.sort()

'''
Exercise 8
'''
L=[1,7,3,9]
M = L.sort()

'''
Exercise 9
'''

F= open('tab.txt','w')
F.write('2\t4\n3\t6')
