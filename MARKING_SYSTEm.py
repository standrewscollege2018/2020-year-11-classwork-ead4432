""" This Program takes your score and tells you if you got A, B, C """

#Setting the scores for the different grades
A = 90

B = 70

C = 50

#Collecting your score
user_score = int(input("What score did you get"))

#Checking if it is a pass grade
if user_score >= 101 or user_score < 0:
    print("The test maximum score was 100 and the minimum was 0 your a muppet")
elif user_score >= 90:
    print("You got an A!")
elif user_score >= 70:
    print("You got a B")
elif user_score >= 50:
    print("You got a C")
elif user_score >= 1:
    print("You didn't pass your a failure")
else:
    print("Wow you had a shocker better luck next time")
    