from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  # example {"Angela" 12, "James": 143"}
  for bidder in bidding_record:
    # find the value
    bid_amount = bidding_record[bidder]
    # find the highest bid
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")
    
while not bidding_finished:
  name = input("Write your name: ")
  price = int(input("What is your bid? $"))
  bids[name] = price
  should_continue = input("Are there any other bidder? Type yes or no.")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    # It clears the screen
    clear()


