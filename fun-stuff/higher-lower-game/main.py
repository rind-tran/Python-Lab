from art import logo, vs
import random
from game_data import data
from replit import clear

# Global variables
score = 0

# Flags
end_game = False

### Function ###
def print_item(data_position):
  name = data[data_position]["name"]
  desc = data[data_position]["description"]
  country = data[data_position]["country"]
  print(f"{name}, a {desc}, from {country}")

def compare_follower(data_position1, data_position2):
  if data[data_position1]["follower_count"] > data[data_position2]["follower_count"]:
    return "A"
  else:
    return "B"

### Main progarm ###

print(logo)

number_b = random.randint(0,len(data)-1)

while not end_game:

  # number a is now number b. Generate new item into number b
  number_a = number_b
  while number_a == number_b:
    number_b = random.randint(0,len(data)-1)
  print_item(number_a)
  print(vs)
  print_item(number_b)
  user_pick = input("Who has more followers: Type 'A' or 'B': ")
  result = compare_follower(number_a,number_b)

  # Clear screen
  clear()
  
  if user_pick == result:
    score += 1
    print(f"Correct. Your score is: {score}")
  else:
    print("You lose.")
    print(f"Your score is: {score}")
    end_game = True