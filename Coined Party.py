# imports
import random
import time

# Functions
def look_away(round1, round2, round3):
    # Variables
    score = 0
    round1 = int(round1)
    round2 = int(round2)
    round3 = int(round3)
    ...

    # --- AI Bot 1 (GPT) ---
    GPT_AImove1 = random.randint(1,4)
    GPT_AImove2 = random.randint(1,4)
    GPT_AImove3 = random.randint(1,4)
    ...

    # --- AI Bot 2 (LLaMA) ---
    LLaMA_AImove1 = random.randint(1,4)
    LLaMA_AImove2 = random.randint(1,4)
    LLaMA_AImove3 = random.randint(1,4)
    ...

    # Round 1 - Preparations
    print("Round 1, Begin!")
    print("Calculating GPT move...")
    time.sleep(0.8)
    print("Calculating LLaMA move...")
    time.sleep(0.8)

    # Round 1 - Comparisons
    if round1 == GPT_AImove1 or round1 == LLaMA_AImove1:
        winner = "Bot"
    else:
        winner = "Player"

    print(f"GPT: {GPT_AImove1}, "
          f"LLaMA: {LLaMA_AImove1}, "
          f"Player: {round1}, "
          f"Winner: {winner} \n")
    ...

    # Round 2 - Preparations
    print("Round 2, Begin!")
    print("Calculating GPT move...")
    time.sleep(0.8)
    print("Calculating LLaMA move...")
    time.sleep(0.8)

    # Round 2 - Comparisons
    if round2 == GPT_AImove2 or round2 == LLaMA_AImove2:
        winner = "Bot"
    else:
        winner = "Player"
    print(f"GPT: {GPT_AImove2}, "
          f"LLaMA: {LLaMA_AImove2}, "
          f"Player: {round2}, "
          f"Winner: {winner} \n")
    ...

    # Round 3 - Preparations
    print("Round 3, Begin!")
    print("Calculating GPT move...")
    time.sleep(0.8)
    print("Calculating LLaMA move...")
    time.sleep(0.8)

    # Round 3 - Comparisons
    if round3 == GPT_AImove3 or round3 == LLaMA_AImove3:
        winner = "Bot"
    else:
        winner = "Player"
    print(f"GPT: {GPT_AImove3}, "
          f"LLaMA: {LLaMA_AImove3}, "
          f"Player: {round3}, "
          f"Winner: {winner} \n")
    ...

    # Calculating Score
    if GPT_AImove1 == round1 or LLaMA_AImove1 == round1:
        if GPT_AImove2 == round2 or LLaMA_AImove2 == round2:
            if GPT_AImove3 == round3 or LLaMA_AImove3 == round3:
                score += 0
            elif GPT_AImove3 != round3 and LLaMA_AImove3 != round3:
                score += 10
            ...
        elif GPT_AImove2 != round2 and LLaMA_AImove2 != round2:
            if GPT_AImove3 == round3 or LLaMA_AImove3 == round3:
                score += 10
            elif GPT_AImove3 != round3 and LLaMA_AImove3 != round3:
                score += 20
            ...
        ...
    elif GPT_AImove1 != round1 and LLaMA_AImove1 != round1:
        if GPT_AImove2 == round2 or LLaMA_AImove2 == round2:
            if GPT_AImove3 == round3 or LLaMA_AImove3 == round3:
                score += 10
            elif GPT_AImove3 != round3 and LLaMA_AImove3 != round3:
                score += 20
            ...
        elif GPT_AImove2 != round2 and LLaMA_AImove2 != round2:
            if GPT_AImove3 == round3 or LLaMA_AImove3 == round3:
                score += 20
            elif GPT_AImove3 != round3 and LLaMA_AImove3 != round3:
                score += 30
            ...
        ...
    ...

    print(f"Total coins: {score}\n")
    time.sleep(1.25)
...

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


'''                           --- Start of Code ---                            '''

# Welcome Message
print("Welcome to Coined Party! \n"
      "It's time for YOU to play some party GAMES! Here are the rules: \n"
      "We'll play the following games in order: \n"
      "    - Look Away \n"
      "    - Slot Machine \n"
      "    - Pig \n"
      "The objective is to gather as many coins as you can by the end of the party!"
      "\n\n")
time.sleep(7)

# Game 1 Message
print("Time for the FIRST game! Look away! The rules to the game are simple. \n"
      "You are going to play against two bots, one named GPT, and the other LLaMA. \n"
      "Then, you choose a direction, either up, down, left, or right. \n"
      "If any of the bots look in the same direction as you, you lose =( \n"
      "If you look in a different direction than them, you WIN =D \n"
      "To look towards a specific direction, we use numbers: \n"
      "1 = up \n2 = down \n3 = left \n4 = right\n Use this as a cheat sheet."
      "\n\n")
time.sleep(6)

# Starting Game 1
print("Without further ado, let's BEGIN!")
move1 = input("Please choose a direction for round 1: ")
time.sleep(0.7)
move2 = input("Thank you! Now, please choose a direction for round 2: ")
time.sleep(0.7)
move3 = input("Thank you! Lastly, please choose a direction for round 3: ")

# Deriving 1
look_away(move1, move2, move3)

# Game 2 Message
print("Time for the SECOND game! Slot Machine! Here are the rules: \n"
      "You give your bet, and a randomized slot machine will display three \n"
      "emojis. If the emojis are all different, you get nothing. If two of the \n"
      "emojis are the same, your bet will double. Lastly, if all three of the \n"
      "emojis are the same, your bet will QUINTIPLE!")
time.sleep(5)

# Starting Game 2
bet = input("Let's begin! I need to know first, how much will you be betting today? ")
time.sleep(0.7)

# Deriving 2
slot_machine(bet)