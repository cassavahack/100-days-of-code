import random

#Get user move
user_input =int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

#Get and print computer move
computer_move = random.randint(0,2)
print(f"computer chose{computer_move}")

#display user move
print(f"you chose{user_input}")

#game logic
if user_input >= 3 or user_input<0:
    print("invalid entry try again")
elif user_input == 0 and computer_move == 2:
    print("You win!")
elif computer_move == user_input:
    print("Its a draw")
elif computer_move > user_input:
    print("You Lose")
elif user_input > computer_move:
    print("You win!")
elif user_input == 0 and computer_move == 2:
    print("You win!")


