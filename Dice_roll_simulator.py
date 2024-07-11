from numpy import array  # Importing the array function from numpy
from random import randint  # Importing the randint function from random

def rolls(num, roll, sides):
    # Function to roll 'num' dice, each with 'sides' sides, and store the results in 'roll'
    for i in range(num):
        roll[i] = randint(1, sides)  # Assigning a random integer between 1 and 'sides' to roll[i]
    return roll  # Returning the updated roll array

if __name__ == "__main__":
    num = int(input("number of dice rolls : "))  # Asking user for the number of dice rolls
    while num <= 0:
        print("Number of rolls must be a positive integer.")
        num = int(input("number of dice rolls : "))

    sides = int(input("number of sides on the dice : "))  # Asking user for the number of sides on the dice
    while sides <= 0:
        print("Number of sides must be a positive integer.")
        sides = int(input("number of sides on the dice : "))

    roll = array([0] * num)  # Initializing an array of zeros with length 'num'
    
    print(rolls(num, roll, sides))  # Printing the result of the rolls function
