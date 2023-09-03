import random
import string

print("Welcome to the PyPassword Generator!")
letters = input("How many letters would you like in your password?\n")
symbols = input("How many symbols would you like?\n")
numbers = input("How many numbers would you like?\n")

alphabet = list(string.ascii_letters)
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
sym = ['!', '@', '#', '$', '%', '^', '&', '*', '_', '-', '+', '=']

password = []

for l in range(1, (int(letters) + 1)):
    c = random.randrange(1, len(alphabet), 1)
    password.append(alphabet[c])

for s in range(1, (int(symbols) + 1)):
    d = random.randrange(1, len(sym), 1)
    password.append(sym[d])

for n in range(1, (int(numbers) + 1)):
    e = random.randrange(1, len(nums), 1)
    password.append(nums[e])

random.shuffle(password)
final_pass = ''.join(password)

print(f"Your password is: {final_pass}")
