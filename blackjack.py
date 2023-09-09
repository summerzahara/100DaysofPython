import random
from blackjack_art import logo
import subprocess


def deal_card(hand):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    hand.append(random.choice(cards))


def calculate_score(hand):
    if len(hand) == 2 and sum(hand) == 21:
        return 0
    for card in hand:
        if card == 11 and sum(hand) > 21:
            hand.remove(11)
            hand.append(1)
    else:
        return sum(hand)


def check_for_winner(users_score, comps_score):
    if comps_score == 0:
        return True, "The computer has Blackjack! You lose."
    elif users_score == 0:
        return True, "Blackjack! You win."
    elif users_score > 21:
        return True, "You have gone over 21. You Lose"
    elif comps_score > 21:
        return True, "Computer has gone over 21. You Win"
    else:
        return False, "No winner yet!"


def final_check(users_score, comps_score):
    if comps_score == 0:
        return True, "The computer has Blackjack! You lose."
    elif users_score == 0:
        return True, "Blackjack! You win."
    elif users_score > 21:
        return True, "You have gone over 21. You Lose"
    elif comps_score > 21:
        return True, "Computer has gone over 21. You Win"
    elif comps_score == users_score:
        return True, "Draw"
    elif comps_score == 21 and users_score < 21:
        return True, "Computer has won."
    elif users_score == 21 and comps_score < 21:
        return True, "You win!"
    elif users_score > comps_score:
        return True, "You win!"
    elif comps_score > users_score:
        return True, "You win!"


def clear_screen():
    subprocess.run("clear", shell=True)


def play_blackjack():
    user_hand = []
    comp_hand = []
    play_game = True

    # Game Logo
    print(logo)

    # Starting Hand
    for x in range(2):
        deal_card(user_hand)
        deal_card(comp_hand)

    while play_game:
        # Initial Score
        user_score = calculate_score(user_hand)
        comp_score = calculate_score(comp_hand)

        # Display to user
        print(f"Your cards: {user_hand}, current score: {user_score}\nComputer's first card: {comp_hand[0]}")

        # Check for winner
        if check_for_winner(user_score, comp_score)[0]:
            status = check_for_winner(user_score, comp_score)[1]
            print(status)
            play_game = False
        else:

            play = input("Type 'y' to get another card, type 'n' to pass: ")
            if play == 'y':
                deal_card(user_hand)
                while comp_score < 16:
                    deal_card(comp_hand)
                    comp_score = sum(comp_hand)
            else:
                print(f"    Your final hand: {user_hand}, final score: {user_score}")
                print(f"    Computer's final hand: {comp_hand}, final score: {comp_score}")
                print(final_check(user_score, comp_score)[1])
                play_game = False


start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
while start_game == 'y':
    # clear_screen()
    play_blackjack()
