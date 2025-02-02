def find_winner(bid_dictionary):
    highest_bid = 0
    winner = ""
    
    for bidder, bid_amt in bid_dictionary.items():
        if bid_amt > highest_bid:
            highest_bid = bid_amt
            winner = bidder
    
    return winner, highest_bid


bid = {}


while True:
    name = input("What is your name? \t")
    price = int(input("What is your bid?: \t$"))
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no': \t").lower()

    bid[name] = price
    if more_bidders == 'yes':
        print("\n" * 100)  
    else:
        break

winner, highest_bid = find_winner(bid)
print(f"\nThe winner is {winner} with a bid of ${highest_bid}")