""" This program creates a silent auction dictated by the user """

#set the variables
highest_bidder = "bob"

highest_bid = 0

bid_continue = True

bid_item = input("enter item name")

reserve_price = int(input("Enter the reserve price"))

while bid_continue == True:
    name = input("enter your name")
    bid = int(input("Enter your bid"))    
    if name == "admin" and bid == 7823:
        print("The auction is over. The", bid_item, "goes to", highest_bidder, "for $", highest_bid)
        bid_continue = False 
    else:
        if bid >= highest_bid:
            highest_bid = bid
            highest_bidder = name
            print("The highest bidder is", name, "and their bid is", highest_bid)
        else:   
            print("The highest bidder is", highest_bidder, "and their bid is", highest_bid)
    
if highest_bid > reserve_price:
    print("The", bid_item, "will not be sold today", highest_bidder, "failed to pay enough money they thought", highest_bid, "was enough")