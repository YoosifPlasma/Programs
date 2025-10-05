# imports
import random

# Pig function
def pig_dice(threshold):
    # Generating Dice
    diceTotal = 0
    roll1 = []
    roll2 = []

    for x in range(10000):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        diceTotal = diceTotal + dice1 + dice2
        roll1 += [dice1]
        roll2 += [dice2]

        print(dice1, dice2)
        if dice1 == 1 or dice2 == 1:
            if dice1 == 1 and dice2 == 1:
                status = "Catastrophic Loss"
                diceTotal = -1
                break
            else:
                status = "Loss"
                diceTotal = 0
                break
        elif diceTotal >= threshold:
            status = "Win"
            break
        elif diceTotal < threshold:
            status = "Proceed"
            continue
        else:
            print("invalid")
            break
        ...
    ...

    # Generating Output
    print("Rolls:", end=" ")
    for i in range(len(roll1)):
        print(f"({roll1[i]}, {roll2[i]}),", end=" ")
    if status == "Win":
        print(f"{status}, ({diceTotal} points).")
    else:
        print(status)
    ...

    # Points Return
    print(f"Points: {diceTotal}.")
...

pig_dice(10)