# Cristian Garcia
# 10/29/24

#Problem 1 prints 10 random intigers between 25 and 35

#Imports the random module
import random

#Stores random numbers
rand_nums = []

#loop to give you 10 random numbers
for _ in  range (10):
    #Gives a random number between 25 and 35
    num = random.randrange (25, 36)
    #Append number to list
    rand_nums.append(num)
    #Prints the random number
    print (num)
    #Prints the list of all random numbers
    print ("List of random numbers:", rand_nums)