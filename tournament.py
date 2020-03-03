"""This program takes the input from a user and does a tournmet points calculation"""
#import random
import random 
#i
i = 0
#point
points = 0 
#keepasking
keep_asking = True
#loop
loop = True
#opponentslist
opponents = []
#team name
team_name = input("Enter your team name")
#welcome
print("**Opponents**")

while keep_asking == True:
    opponent = input("enter an opposing team")
    opponent.lower
    if opponent == "done":
        keep_asking = False
    else:
        opponents.append(opponent)

for i in range(len(opponents)):
    print("Game", i+1, team_name, "vs", opponents[i])
    score_team = int(input("What score did your team get"))
    score_opponent = int(input("What score did the opponent get"))
    if score_team > score_opponent:
        print(team_name, "Wins Game", i+1, score_team, "to", score_opponent)
        points = points+3
    elif score_opponent > score_team:
        print(opponents[i], "Wins Game", i+1, score_opponent, "to", score_team)
        points = points+1
    else:
        print("It was a draw", score_team, "points each")
        points = points+2
print("well done your team got", points, "points")
        
    