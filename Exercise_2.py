# Excercise 2

#1
s = "fire and ice"

#2
print (s[2])

#3
print (s[4])

#4
print (s[9])
print (s[-1])
print (s[-2])

#5
import math
for n in (0,1,2,3,4,5,6,7,8,9,10,11):
	c = n%2
	if (c==0):
		print (s[c])
		n=n+1
	else:
		n=n+1

#6
import math
for n in (0,1,2,3,4,5,6,7,8,9,10,11):
	c= n%2
	if (c!=0):
		print (s[c])
		n=n+1
	else:
		n=n+1

#7
import math
for n in (0,6):
	print (s[n])

#8
print (s[::-1])

#9
s.count('i')
s.count('e')

#11
s.find('fire')

#12
s.find('re and')

#13
s.find('re &')

#14
print (s.find('e'))

#15
print (s.rfind('e'))

#16
s= "may the force be with you"
print (s[3])
print (s[6])
print (s[9])
print (s[-1])
print (s[-2])

import math
for n in (0,12):
	c=n%2
	if (c==0):
		print (s[c])
		n=n+1
	else:
		n=n+1

import math
for n in (0,12):
	c=n%2
	if (c!=0):
		print (s[c])
		n=n+1
	else:
		n=n+1

import math
for n in (0,6):
	print (s[n])

print (s[::-1])
s.count('i')
s.count('e')

print (s.rfind('e'))

#17
s= '234​ 4329​​ 7654​ 8923'

#18
new_s= ''
spl = s.split()
a0 =''
a1 =''
a2 =''
a3 =''

for i in spl:
	print(spl.index(i))
	if (spl.index(i))==0:
		a0 = (str(int(i[0]+3))+(str(int(i[1]+3)))+(str(int(i[2]+3))))
	elif (spl.index(i))==1:
		a1 = (str(int(i[0]+3))+(str(int(i[1]+3)))+(str(int(i[2]+3)))+(str(int(i[2]+3))))
	elif (spl.index(i))==2:
		a2 = (str(int(i[0]+3))+(str(int(i[1]+3)))+(str(int(i[2]+3)))+(str(int(i[2]+3))))
	else:
		a3 = (str(int(i[0]+3))+(str(int(i[1]+3)))+(str(int(i[2]+3)))+(str(int(i[2]+3))))

print (a0+" "+a1+" "+a2+" "+a3)
