"""this program takes a series of number and gives you the mean of the nummbers"""
#make a list
numbers = []
#keepasking
keep_asking = True
while keep_asking == True:
    number = float(input("Enter a number"))
    if number == -1:
        keep_asking = False
        print("The mean is", sum(numbers)/len(numbers))
    else:
        numbers.append(number)
    
    