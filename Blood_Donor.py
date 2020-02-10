""" This program tells you if you are eligable for a blood donorship """

#Setting the age 
AGE = 16

#Setting the weight
WEIGHT = 50

#Welcome message
print("Welcome to blood donorship central")

#Getting the users age
age_user = int(input("What is you age"))

#Checking if they are eligable
if age_user < AGE:
    print("You are not eligable for the donorship")
else:
    weight_user = int(input("What is your weight"))
    
    if weight_user < WEIGHT:
        print("You are not eligble for blood donorship")
    else:
        print("You are eligable to have your blood drained")