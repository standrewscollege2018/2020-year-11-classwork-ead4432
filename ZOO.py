""" This Program informs you if you have to pay the child fees for the zoo """

CHILD_AGE = 13
CHILD_PRICE = 15
keep_asking = True

while keep_asking == True:
    try:
        child_age = int(input("What is your age"))        
        if child_age <= CHILD_AGE:
            print("You must pay the Child price which is $", CHILD_PRICE)
            keep_asking = False
        else:
            print(" Welcome senior citizen you do not need to pay the child price ")
        
            print("Welcome to the zoo")
            keep_asking = False
    except:
        print("Error 01110011 01110100 01110101 01110000 01101001 01100100 Invalid user")