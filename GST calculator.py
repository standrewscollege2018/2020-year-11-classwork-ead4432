"""This program gets an item name and price and then adds GST to the item price"""

#we need to create an variable that is the input of the user
item = input("What would you like to buy")

#we than need to set the item_price variable to another input result
item_price = float(input("How much does your item cost"))

#we need to print the item variable with the item_price variable times 1.5
print(item, "will cost you $", item_price * 1.5, "with GST added onto it")