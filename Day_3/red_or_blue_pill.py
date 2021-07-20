# Starts the game.
print("Welcome to Treasure Island!\n Your mission is to find the treasure...")

# Inital question.
left_or_right = input("left or right? ")

if left_or_right.lower() == "left":
    swim_or_wait = input("swim or wait? ")
    if swim_or_wait.lower() == "wait":
        color_door = input("Which door? Red/Blue/Yellow? ")
        if color_door.lower() == "yellow":
            print("You win!!")
        elif color_door.lower() == "red":
            print("Ouch...you're ingulfed in fire.\n Game Over.")
        elif color_door.lower() == "blue":
            print("Yuck...you're eaten by beasts.\n Game Over.")
        else:
            print("Game Over.")
    else:
        print("You were eaten by a...trout.\n Game Over.")
else:
    print("Oops, you fell in a hole...\n Game Over.")
    