""" This program runs a series of numbers from a user chosen start number and end number """

#get the start+end numbers
start = int(input("Choose a starting number"))

end = int(input("Choose a end number"))

if start < end:
    increment = 1
else:
    increment = -1


#forloop
for i in range (start, end+increment, increment):
    print(i)
