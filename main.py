rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

play = [rock, paper, scissors]

human_locked_pick = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(play[human_locked_pick])

computer_locked_pick = random.randint(0, 2)
print(f"Computer chose:\n {play[computer_locked_pick]}")

#rock
if human_locked_pick == 0:
    if computer_locked_pick == 0:
        print("It's a tie")
    elif computer_locked_pick == 1:
        print("You lose")
    else:
        print("You Win")

#paper
if human_locked_pick == 1:
    if computer_locked_pick == 0:
        print("You Win")
    elif computer_locked_pick == 1:
        print("It's a tie")
    else:
        print("You lose")

#scissors
if human_locked_pick == 2: 
    if computer_locked_pick == 0:
        print("You lose")
    elif computer_locked_pick == 1:
        print("You win")
    else:
        print("It's a tie")