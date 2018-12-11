# average_function.py
# For this exercise the pseudo-code is required (in this same file) 
# Write a function that calculates the average of the values of
# any vector of 10 numbers 
# Each single value of the vector should be read from the keyboard
# and added to a list.
# Print the input vector and its average 
# Define separate functions for the input and for calculating the average

'''
pseudo-code:
'''

'''
I'm defining a funtion that compute the Average of a Vector
'''

def Average(v):
'''
I create a counter Sum
'''
	Sum=0
	for n in range(10):
		Sum=Sum+v[n]
		Average=(Sum)/10
'''
In that for cicle the function compute the average
'''
	print (f"The input vetor is: {v}")
	print (f"The average of this vector is: {Average}")

'''
Now there are input for function
'''

values = input("Write values of vector with space between numbers: ")
V = list(map(int, values.split()))

Result = Average(V)
print (Result)
