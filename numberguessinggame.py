import random
from guess_art import icon

print(icon)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard': ")

number = random.randrange(1, 100)
game_active = True


def guess_number(turns):
    print(f"You have {turns} turns left.")
    g = int(input("Make a guess: "))
    return g


def calc_turns(level):
    turns = 0
    if level == "easy":
        turns += 10
        return turns
    elif level == "hard":
        turns += 5
        return turns


turn = calc_turns(level)

while game_active:

    guess = guess_number(turn)

    if guess == number:
        print(f"The number is {number}, You win!")
        game_active = False
    elif guess != number:
        if guess > number:
            print("Too high")
        else:
            print("Too low")
        turn -= 1
        if turn != 0:
            continue
        else:
            print(f"The number is {number}, You Lose!")
            game_active = False
