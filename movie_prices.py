""" This program calculates how much a movie ticket is for you """

#are they a student
student_status = input("Are you a student y/n")

#get the user age
user_age = int(input("What is your age"))

#give them their price
if student_status == "y":
    print("Ticket price is $8")
elif user_age < 5:
    print("You need not pay")
elif user_age >= 18:
    print("the price is $12")
elif user_age >= 13:
    print("The price is $9")
elif user_age >= 5:
    print("The price is $7")


