import os

def secret_auction():
    bids = {}
    top_bid = 0
    winner = {}
    other_players = True
    first_auctioneer = input("What is your name? ")
    first_auctioneer_bid = int(input("What is your bid? $"))
    bids[first_auctioneer] = first_auctioneer_bid
    os.system('clear')
    second_auctioneer = input("What is your name? ")
    second_auctioneer_bid = int(input("What is your bid? $"))
    bids[second_auctioneer] = second_auctioneer_bid
    os.system('clear')
    while other_players:
        other_auctioneers = input("Is there another bid? (y/n) ")
        if other_auctioneers == "y":
            third_auctioneer = input("What is your name? ")
            third_auctioneer_bid = int(input("What is your bid? $"))
            bids[third_auctioneer] = third_auctioneer_bid
            os.system('clear')
        else:
            other_players = False
    for key in bids:
        if bids[key] > top_bid:
            top_bid = bids[key]
            winner = [key, bids[key]]
    print(f"The winner is {winner[0]} with a bid of ${winner[1]}!")
    

secret_auction()