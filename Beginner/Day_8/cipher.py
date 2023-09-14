from cipher_art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)


def caesar(_direction, _text, _shift):
    reveal_word = ""
    if _direction == "decode":
        _shift *= -1
    for character in _text:
        if character in alphabet:
            index = alphabet.index(character)
            new_letter = alphabet[index + _shift]
            reveal_word += new_letter
        else:
            reveal_word += character
    print(f"The {_direction}ed text is {reveal_word}")


game_active = True

while game_active:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(_direction=direction, _text=text, _shift=shift)
    play_again = input("Do you want to play again? (Yes or No)\n").lower()
    if play_again == "no":
        game_active = False
        print("Goodbye")
