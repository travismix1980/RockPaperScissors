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

computer_options = ["r", "p", "s"]
computer_choice = random.choice(computer_options)


print("Welcome to Rock Paper Scissors\n")
print("##############################\n\n")
player_choice = input("Enter 'r' for rock, 'p' for paper and 's' for scissors: ")

# set player choice to lower case
player_choice = player_choice.lower()

# spacing
print("\n\n")

# print player choice 
if player_choice == "r":
    print("Player chose rock!")
    print(rock)
elif player_choice == "p":
    print("Player chose paper!")
    print(paper)
elif player_choice == "s":
    print("Player chose scissors!")
    print(scissors)
# error 
else:
    print("Not a valid choice")

# print computer choice
if computer_choice == "r":
    print("Computer chose rock!")
    print(rock)
elif computer_choice == "p":
    print("Computer chose paper!")
    print(paper)
elif computer_choice == "s":
    print("Computer chose scissors!")
    print(scissors)

# Game Logic to determine winner
if player_choice == computer_choice:
    print("We have a tie")

# player chose rock
elif player_choice == "r":
    if computer_choice == "p":
        print("Computer wins!!!")
    elif computer_choice == "s":
        print("Player wins!!!")

# player chose paper
elif player_choice == "p":
    if computer_choice == "r":
        print("Player wins!!!")
    elif computer_choice == "s":
        print("Computer won!!!")

# player chose scissors
elif player_choice == "s":
    if computer_choice == "r":
        print("Computer won!!!")
    elif computer_choice == "p":
        print("Player won!!!")