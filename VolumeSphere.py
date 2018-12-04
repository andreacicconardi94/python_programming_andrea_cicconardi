# This script calculates the volume of a sphere and print it to the screen
from math import pi
D= raw_input("set the diametre: ")
R= float(D)/2.0
V= (4.0/3.0)*pi*(R**3)
print("Volume of the sphere is: %f "%V)
