#DAY 3 is on if...else
print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1=input("You have reached a crossroad. Pick a side either 'left' or 'right'").lower()

if choice1=='left':
    choice2=(input("You are in a new hell. Will you 'swim' or 'wait'?"))
    if choice2=='wait':
        choice3= (input("You have entered a dungeon with three doors."
                        "Now you gotta pick a door to go through."
                        "Either the 'red', 'yellow' or 'blue' door ").lower())
        if choice3=='red':
            print("You opened the door to a furnace. You got burnt by fire!")
        elif choice3=='yellow':
            print("You found the exit. You win my nigga!!")
        elif choice3=='blue':
            print("You opened the cage to a beast. You got eaten by beasts")
        else:
            print("Game over!!")
    else:
        print("Nigga fell into a hole")
else:
    print("You fell into a hole. Game over!")


