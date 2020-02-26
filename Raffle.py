""" This program takes input and does a raffle generator with it """
#import random
import random 
#make a list
participants = []
#make a variable for the prize + value
prize = input("What is the prize being raffled?")
value = int(input("What is the prize valued at?"))
#variable
i = 0
#keep_asking
keep_asking = True
#while loop
while keep_asking == True:
    raffle_entrant = input("Enter a contestant")
    i = i+1
    if raffle_entrant == "done" or raffle_entrant == "Done":
        keep_asking = False
    else:
        participants.append(raffle_entrant)
print(participants[random.randint(0,i)], "Won the", prize, "valued at $", value)