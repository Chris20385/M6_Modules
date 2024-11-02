# Cristian Garcia
# 10/29/24

#Problem 4 Caculates the factorial of a intiger

#Import math module to use math functions
import math 

#Ask user for intiger input to calculate factorial
user_input = int(input("Use a intiger to calculate its factorial:"))

#Calculate factorial using math module
factorial_math = math.factorial(user_input)

#Set a variable to calculate factorial manually
factorial_munua1 = 1

#Loop to calculate factorial manually
for i in range(1, user_input +1):
    factorial_munua1 *= i

#Print results from math mudule
print (f"Factorial calculate using math factorial: {factorial_math}")

#Print results from manual calculations
print (f"Factorial calculate using manually {factorial_munua1}")

#Chack that both methods give the same results
if factorial_math == factorial_math:
    print ("Both methods give the same results")
else:
    print ("The results are differnt")