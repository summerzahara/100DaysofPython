# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

with open("./Input/Letters/starting_letter.txt", "r") as letter:
    content = letter.readlines()
    with open("./Input/Names/invited_names.txt", "r") as invited:
        names = invited.readlines()
        invitee = []
        for name in names:
            invite = name.strip()
            invitee.append(invite)
    for person in invitee:
        with open(f"./Output/ReadyToSend/letter_for_{person}.txt", "w") as new_letter:
            for item in content:
                new_item = item.replace("[name]", f"{person}")
                new_letter.write(new_item)
