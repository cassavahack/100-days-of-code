import random

print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100.")

easy_or_hard = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

SECRET_NUMBER = random.randint(1, 100)
print(f"the test num is {SECRET_NUMBER}")

if easy_or_hard == "easy":

   lives = 10

   if lives == 0:
       print(f"game over you list number was {SECRET_NUMBER}")
   while lives > 0:
       guess = int(input("guess a number"))
       if guess == SECRET_NUMBER:
           print("Guess was successful you win!!!!!")
           break
       else:
           lives -=1
       if guess > SECRET_NUMBER:
            print("number too high try again")
       if guess < SECRET_NUMBER:
           print("number too low try again")
       if lives ==0:
            print(f"game over, the number was {SECRET_NUMBER}")
       print(f"You have {lives} guesses left")

if easy_or_hard == "hard":
     lives = 5

     if lives == 0:
         print(f"game over you list number was {SECRET_NUMBER}")
     while lives > 0:
         guess = int(input("guess a number"))
         if guess == SECRET_NUMBER:
             print("Guess was successful you win!!!!!")
             break
         else:
             lives -= 1
         if guess > SECRET_NUMBER:
             print("number too high try again")
         if guess < SECRET_NUMBER:
             print("number too low try again")
         if lives == 0:
             print(f"game over, the number was {SECRET_NUMBER}")
         print(f"you have {lives} guess left")
