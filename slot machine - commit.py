# imports
import random

# Slot Machine Function
def slot_machine(bet):
    # Randomizing slots
    slot1 = random.randint(1, 4)
    slot2 = random.randint(1, 4)
    slot3 = random.randint(1, 4)
    ...

    # Assigning emoji to Slot 1 based off random number
    if slot1 == 1:
        slot1 = "🤪"
    elif slot1 == 2:
        slot1 = "😍"
    elif slot1 == 3:
        slot1 = "😭"
    elif slot1 == 4:
        slot1 = "😁"
    else:
        print("invalid")
        slot_machine(bet)
    ...

    # Assigning emoji to Slot 2 based off random number
    if slot2 == 1:
        slot2 = "🤪"
    elif slot2 == 2:
        slot2 = "😍"
    elif slot2 == 3:
        slot2 = "😭"
    elif slot2 == 4:
        slot2 = "😁"
    else:
        print("invalid")
        slot_machine(bet)
    ...

    # Assigning emoji to Slot 3 based off random number
    if slot3 == 1:
        slot3 = "🤪"
    elif slot3 == 2:
        slot3 = "😍"
    elif slot3 == 3:
        slot3 = "😭"
    elif slot3 == 4:
        slot3 = "😁"
    else:
        print("invalid")
    ...

    # Determining score
    if (slot1 == slot2 or slot1 == slot3 or slot2 == slot3) and not(slot1 == slot2 and slot1 == slot3):
        bet *= 2
    elif slot1 == slot3 and slot1 == slot3:
        bet *= 5
    else:
        bet = 0

    print(f"{slot1} {slot2} {slot3},  {bet}")
...

slot_machine(30)