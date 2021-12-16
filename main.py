# The below function plays Rock, Paper or Scissors with you
# Created by Agamdeep Singh / CodeWithAgam
# Youtube: CodeWithAgam
# Github: CodeWithAgam
# Instagram: @agamdeep_21, @coderagam001
# Twitter: @CoderAgam001
# Linkdin: Agamdeep Singh

# The random moudule generates a random number
import random

# Define Rock, Paper, and Scissors as ASCII arts
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

# Print a welcome message
print("Welcome to Rock, Paper or Scissors!\n")

# Get the inputs from the user
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# Define a random number chosen by the computer
computer_choice = random.randint(0, 2)

# If the user chose Rock, the below condition gets executed 
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

# If the user chose Paper, the below condition gets executed   
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

# If the user chose Scissors, the below condition gets executed   
elif user_choice == 2:
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

# Print this message if the user typed a number other than 0, 1 or 2
else:
  print("You typed an invalid number, You Lose!")