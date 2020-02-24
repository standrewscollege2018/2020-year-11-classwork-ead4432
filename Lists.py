"""This program demonstrates how lists work, including how to print, change and append items """

#lists always have square brackets. Items are separated by commas
names = ["Rico", "Ethan", "Ben"]
#print the whole list
print(names)
#print the nuber of items in list
print(len(names))
#name the list and the position in the list to get a specific item.
print(names[2])
#change an item in the list
names[0] = "henry"
print(names)
#to insert an item at a specific location use insert(index, item)
names.insert(0, "Rico")
print(names)
#to add an item at the end of the list
names.append("Benji")
print(names)
