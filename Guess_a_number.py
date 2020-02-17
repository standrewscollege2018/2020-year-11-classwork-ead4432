""" This program plays the game guess a number """

#set a boolean variable
keep_asking = True 

#pick a random number
import random
number = random.randint(-100, 100)

#count how many guesses they had
guess_count = 0

#assaign a variable to the input
guess = float(input("Guess a number"))

while keep_asking == True:

    if guess > number:
        print("Smaller")
        guess = float(input("Guess a number"))
        guess_count = guess_count+1
    elif guess < number:
        print("Greater")
        guess = float(input("Guess a number"))
        guess_count = guess_count+1
    else:
        print("Thats the number")
        keep_asking = False
        print(guess_count, "guesses")
        
