import random 

# List of possible choices
item_list = ["rock", "paper", "scissor"]

# Input from user
user_choice = input("Enter your move (rock, paper, scissor): ").lower()

# Random choice by computer
comp_choice = random.choice(item_list)

# Print the choices
print(f"User choice = {user_choice}, Computer choice = {comp_choice}")

# Determine the result
if user_choice == comp_choice:
    print("It's a tie!")
elif user_choice == "rock":
    if comp_choice == "scissor":
        print("Rock wins! You win!")
    else:
        print("Paper wins! Computer wins!")
elif user_choice == "paper":
    if comp_choice == "rock":
        print("Paper wins! You win!")
    else:
        print("Scissor wins! Computer wins!")
elif user_choice == "scissor":
    if comp_choice == "paper":
        print("Scissor wins! You win!")
    else:
        print("Rock wins! Computer wins!")
else:
    print("Invalid input! Please choose rock, paper, or scissor.")

















