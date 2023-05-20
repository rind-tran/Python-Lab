from art import logo
import random


### Functions ###
def choose_difficulty():
  choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if choice == "easy":
    return 10
  elif choice == "hard":
    return 5
  else:
    return 5
    
def guess_number(attempts, result_number):
  end_game = False
  lives = attempts
  while not end_game:
    print(f"You have {lives} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == result_number:
      print("You win")
      end_game = True
    else:
      lives -= 1
      if guess > result_number:        
        print("Too high!")
      else:
        print("Too low!")
        
      if lives == 0:
        print("You lose!")
        end_game = True
      else:
        print("Guess again.")

### Main ###
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
guess_number(choose_difficulty(), random.randint(0,100))