# Cristian Garcia
# 10/30/24

#Problem 3 A program that executes a probabilistic event

#Imports the random module
import random

#Function that simulates flipping a coin
def flip_coin(bias=0.84, flips=1000):

    #A list that stores the results of coin flips
    results = []
    
    #Loop for number of flips
    for _ in range(flips):

        # Check if the random number is less than the bias to determine heads or tails
        if random.random() < bias:
            results.append("heads")
        else:
            results.append("tails")
    return results

#Calculates the the percentage of heads in the results
def calculate_percentage(results):
    heads_count = results.count("heads")
    percentage_heads = (heads_count / len(results)) * 100
    return percentage_heads
#Flips the coin
coin_flips = flip_coin()

#Calculates the percentage of heads from the flips
percentage_heads = calculate_percentage(coin_flips)

#Prints the number of flipd
print(f"Total flips: {len(coin_flips)}")

#Prints the count of heads and tails
print(f"Heads: {coin_flips.count('heads')}, Tails: {coin_flips.count('tails')}")

#Prints the percentage of heads
print(f"Percentage of Heads: {percentage_heads:.2f}%")
