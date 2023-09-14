from Beginner.Day_7 import hangman_art, hangman_words
import random

word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
print(chosen_word)
display = []
lives = 6
guessed = []

print(hangman_art.logo)
for n in chosen_word:
    display.append("_")
print(" ".join(display))

while "_" in display:
    guess = input("Guess a letter: ").lower()
    if guess in guessed:
        print(f"You have already guessed {guess}")
    else:
        guessed.append(guess)
    i = 0
    for letter in chosen_word:
        if guess == letter:
            display[i] = letter
        i += 1
    print(" ".join(display))
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
    if lives == 0:
        break
    print(hangman_art.stages[lives])
if lives == 0:
    print(hangman_art.stages[lives])
    print("You Lose.")
else:
    print("You Win.")
