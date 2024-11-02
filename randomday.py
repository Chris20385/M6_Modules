# Cristian Garcia
# 10/29/24

#Problem 2 Selects a random day of the week and prints a message

#Imports the random module
import random

#Contains days of the week Monday to Friday
day_of_the_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")

#Selects a random day
random_day = random.choice(day_of_the_week)

#Prints message with random day selected
print(f"It was a rainy {random_day} and the lightning flashed across the sky")