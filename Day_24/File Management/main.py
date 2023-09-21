# Write to file
with open("my_file.txt", "w") as file:
    file.write("Your mom")

# Append to file
with open("my_file.txt", "a") as file:
    file.write("\nYour mom, again!")

# Read file
with open("my_file.txt", "r") as file:
    content = file.read()
    print(content)

# Create new file
with open("new_file.txt", "w") as file:
    file.write("Tu mama")
