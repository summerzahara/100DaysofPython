import random

play = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))


def roshambo(num):
    moves = ["Rock", "Paper", "Scissors"]

    if play == 0:
        print(f"You chose: {moves[0]}")
    elif play == 1:
        print(f"You chose: {moves[1]}")
    elif play == 2:
        print(f"You chose: {moves[2]}")
    else:
        print("error")
        return 0
    computer = random.randint(0, 2)
    print(f"Computer chose: {moves[computer]}")

    if (play == 0 and computer == 2) or (play == 2 and computer == 1) or (play == 1 and computer == 0):
        print("You win.")
    elif (play == 0 and computer == 1) or (play == 1 and computer == 2) or (play == 2 and computer == 0):
        print("You Lose")
    else:
        print("Draw.")


roshambo(play)
