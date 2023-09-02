print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

def treasure():
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")
    one = input("You are in a maze!! Do you want to go left(L) or right(R)? ").upper()
    if one == "R":
        print("The path behind you closed and you are lost forever. GAME OVER.")
        return 0

    two = input("You made it out of the maze!! Suddenly it has started raining, and the path forward is filled. Do you "
                "want to swim (S), or wait(W)? ").upper()
    if two == "S":
        print("A current has sucked you under. GAME OVER.")
        return 0

    three = input("The path cleared, and you move forward. You reached three doors. Do you go in the:\n red door (R)\n "
                  "the blue door (B)\n or the yellow door (Y)?\n").upper()
    if three == "R" or three == "B":
        print("Oh no, a Dementor! GAME OVER.")
        return 0

    print("You have found the treasure!!")

treasure()
