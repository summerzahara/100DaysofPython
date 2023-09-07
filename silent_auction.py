import subprocess
from silent_auction_art import logo


def clear_screen():
    subprocess.run("clear", shell=True)


def silent_auction():
    auction_active = True
    auction_dict = {}
    while auction_active:
        name = input("What is your name?\n")
        bid = int(input("What is your bid?\n"))
        auction_dict[name] = bid
        prompt = input("Any other bidders?\n")
        if prompt == "no":
            auction_active = False
            winner = ""
            winning_bid = 0
            for final_bid in auction_dict.values():
                if final_bid > winning_bid:
                    winning_bid = final_bid
            for x, y in auction_dict.items():
                if y == winning_bid:
                    winner = x
            print(f"{winner} has won the auction with a bid of ${winning_bid}")
        elif prompt == "yes":
            clear_screen()


print(logo)
silent_auction()
