from replit import clear
#HINT: You can call clear() to clear the output in the console.

import art
print(art.logo)

bids_register ={}
more_bidders = True

def find_highest_bid(bids_register):
  highest_bid = 0
  highest_bidder = None
  for key in bids_register:
      if bids_register[key] > highest_bid:
        highest_bid = bids_register[key]
        highest_bidder = key
  clear()
  print(f"The winner is {highest_bidder} with a bid of ${highest_bid} ")

while more_bidders:
  bidder_name = input("Enter your name: ")
  bid_price = int(input("Enter your bid: "))
  bids_register[f"{bidder_name}"] = bid_price
  extra_bidders = input("Are there any more bidders? yes/no :")
  if extra_bidders == "yes":
    clear()
    continue
  else:
    more_bidders = False
    find_highest_bid(bids_register)
















