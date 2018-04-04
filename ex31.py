print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print(f"Well, doing {bear} is porbably better.")
        print("Bear runs away.")

elif door == "2":
    print(" You see an alter with a emmerald, what do you do?")
    print("1. approach the alter")
    print("2. Go back from where you came")
    print("3. Look for boody traps")
    #print("You stare into the endless abyss at Cthulu's retina.")
    #print("1. Bluberries.")
    #print("2. Yellow jacket clothespin.")
    #print("3. Understanding revolvers yelling melodies.")

    alter = input("> ")

    if alter == "1":
        print("""You take 1, 2, 3, steps towards the alter, you trip a thin wire
         with your feet, a trap door opens and you fall to your death.
         Game Over!""")

    elif alter == "2":
        print("Wimp!")
        print("You are not an adventurer then!")

    elif alter =="3":
        print("You spot the trip wire and step over it to reach the alter")
        print("What do you do now?")
        print("1. Pick up the emmerald and run")
        print("""2. Pick up the emmerald and replace it with a metal ball you have
        in your bag?""")

        emmerald = input("> ")

        if emmerald == "1":
            print("Are you insane!!! Giant hammer comes down and squishes you!")
            print("Better luck next time!")

        elif emmerald == "2":
            print("Now you are channeling your inner Indiana Jones!")
            print("There is hope for you yet.")
            print("WINNER!!")

        else:
            print("This is not an option, please play again!")
    #insanity = input("> ")

    #if insanity == "1" or insanity == "2":
        #print("Your body survives prowered by a mind of jello.")
        #print("Good job!.")
    #else:
        #print("The insanity rots your eyes into a pool of muck.")
        #print("Good job!")

else:
    print("You stumble around and fall on a knife and die. Good job!")
