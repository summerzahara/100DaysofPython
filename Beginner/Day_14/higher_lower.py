from hl_gamedata import data
from hl_art import logo, vs
import random

def pull_data():
    return random.choice(data)

game_active = True
score = 0

a = pull_data()
# print(a)

while game_active:
    b = pull_data()
    # print(b)

    # Display data item 1
    print(logo)
    print(f"Compare A: {a['name']}, {a['description']}, from {a['country']}.")
    # Display data item 2
    print(vs)
    print(f"Against B: {b['name']}, {b['description']}, from {b['country']}.")

    # prompt user for input of choice
    user = input("Who has more followers? Type 'A' or 'B': ").lower()
    if user == "a":
        user = a
    elif user == "b":
        user = b

    # compare followers and select higher -- compare to user input
    if a['follower_count'] > b['follower_count']:
        winner = a
        # print(f"user: {user}, winner: {winner}")
        # print(f"A: {a['follower_count']} > B: {b['follower_count']}")

    else:
        winner = b
        # print(f"user: {user}, winner: {winner}")
        # print(f"B: {b['follower_count']} > A: {a['follower_count']}")
    # if incorrect - end game
    if user == winner:
        print("Correct")
        score += 1
        a = winner
    else:
        game_active = False
        print(f"Sorry, that's wrong. Final score: {score}")
# if correct, keep "winner -select new second opponent
# if correct count score