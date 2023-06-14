#!/usr/bin/env python

#Function to guess the music genre
import random

#Guessing music genre game
def main():
    """Start guessing a music genre game."""
    print("Guess the music genre!")
    print()

# Music genre list
    print("The answer is between rock,pop,indie,beats and rap.")
    print()

    genre = ["rock","pop","indie","beats","rap"]

#Set x to return a random value of genre      
    x = random.choice(genre)

#Set guess to any value of genre
    guess = None

#While loop   
    while x != guess:

#Input from user      
        guess = str(input("Guess which of the music genre I'm thinking of?"))
        print()

#Output received       
        if x == guess:
            print("Congrats, the answer is {}...You have a good music taste!".format(guess))
            print()
        else:
            print("{} is a wrong answer".format(guess))
            print()
        if guess == x:
            print("Congrats,You get [+1 point]")
            print()
        else:
            print("Try again")
            print()
        if guess == x:
            print("Your total point is 1.")
            print()
            

main()
