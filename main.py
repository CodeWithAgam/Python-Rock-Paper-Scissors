# The below function plays Rock, Paper or Scissors with you
# Created by Agamdeep Singh / CodeWithAgam
# Youtube: CodeWithAgam
# Github: CodeWithAgam
# Instagram: @agamdeep_21, @coderagam001
# Twitter: @CoderAgam001
# Linkdin: Agamdeep Singh

import random

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


user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

computer_choice = random.randint(0, 2)

if user_choice == 0:
  print(rock)

  if computer_choice == 0:
    print("Computer chose: \n")

    print(rock)

    print("\nIt's Draw")

  elif computer_choice == 1:
    print("Computer chose: \n")

    print(paper)

    print("\nYou Lose")

  else:
    print(scissors)

    print("\nYou Win")
  
elif user_choice == 1:
  print(paper) 

  if computer_choice == 0:
    print("Computer chose: \n")

    print(rock)

    print("\nYou Win")

  elif computer_choice == 1:
    print("Computer chose: \n")

    print(paper)

    print("\nIt's Draw")

  else:
    print(scissors)

    print("\nYou Lose")
  
else:
  print(scissors)

  if computer_choice == 0:
    print("Computer chose: \n")

    print(rock)

    print("\nYou Lose")

  elif computer_choice == 1:
    print("Computer chose: \n")

    print(paper)

    print("\nYou Win")

  else:
    print(scissors)

    print("\nIt's Draw")