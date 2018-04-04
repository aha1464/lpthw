from sys import exit

# the gold room is the last room at the end of the story
# definition of the the gold room, and print out description
def gold_room():
    print("This room is full of gold. How much do you take?")
# the users choice and the need for an input
    choice = input("> ")
    if "0" in choice or "1" in choice:
        # made a mistake here with < instead of =
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard")


def bear_room():
    print("There is a bear there.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    print("Take the honey or taunt the bear?")

    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")

            bear_moved = True
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")


def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print(why, "Good job!")
    exit(0)

# why is the start almost at the end of the code?
def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which door do you choose, left or right?")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

start()
