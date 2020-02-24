""" This program creates a silent auction dictated by the user """

#set the variables
highest_bidder = "bob"

highest_bid = 0

ask_for_reserve = True

bid_continue = True
#while loop for repeated auction
while ask_for_reserve == True:
   bid_item = input("enter item name:")

   reserve_price = int(input("Enter the reserve price:"))
   
   ask_for_reserve = False

while bid_continue == True:
   #error catching
   try:
         name = input("enter your name:")
         bid = int(input("Enter your bid:"))    
         if name == "admin" and bid == 7823:
          #end bidding  
            bid_continue = False 
         else:   
            if bid > highest_bid:
               highest_bid = bid
               highest_bidder = name
               print("The highest bidder is", highest_bidder, "and their bid is", highest_bid)
            else:   
               print("The highest bidder is", highest_bidder, "and their bid is", highest_bid)
   
   except: #error catch message
      print("Error 01110011 01110100 01110101 01110000 01101001 01100100 Invalid user")


# check if reserve price has been met
if highest_bid < reserve_price:
   print("The", bid_item, "will not be sold today", highest_bidder, "failed to pay enough money they thought", highest_bid, "was enough")
else: #finish auction
   print("The auction is over. The", bid_item, "goes to", highest_bidder, "for $", highest_bid)