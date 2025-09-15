# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
import art
print(art.logo)
names_bids = {}

while True:
    names = input("What is your name: ")

    bids = int(input("What is your bid: $"))
    proceed = input("Are there any other bidders? Type 'yes or no'. \n")

    names_bids[names] = bids

    if proceed.lower() == "yes":
        print("\n" * 20)
    elif proceed.lower() == "no":
        break
    else:
        print("Invalid response. Try again.")
        continue

largest_bid_name = max(names_bids, key =names_bids.get)
largest_bid = max(names_bids.values())


print(f"The winner is {largest_bid_name} with a winning bid of ${largest_bid}")
