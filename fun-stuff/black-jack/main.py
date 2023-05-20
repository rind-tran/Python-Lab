from art import logo
print(logo)
import random

### Variables ###
user_cards = []
computer_cards = []
user_score = 0
computer_score = 0
new_card = 0
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

### Flags ###
another_card = True

### Functions ###
def deal_card():
  return random.choice(cards)

def calculate_score(card_list):
  if sum(card_list) > 21 and 11 in card_list:
    card_list.remove(11)
    card_list.append(1)
  return sum(card_list)

### main program ###

# Pick 2 cards for user and computer
for _ in range(2):
  user_cards.append(deal_card())
  computer_cards.append(deal_card())

# Calculate user score and computer score
user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)  

# Check black jack
if computer_score == 21:
        print(f"Computer card: {computer_cards}, computer score: {computer_score}")
        print("Black Jack! You lose!")
elif user_score == 21:
        print(f"Your card: {user_cards}, current score: {user_score}")
        print(f"Computer card: {computer_cards}, computer score: {computer_score}")
        print("Black Jack! You win!")
else:

  # Show cards to user
  print(f"Your card: {user_cards}, current score: {user_score}")
  print(f"Computer's first card: {computer_cards[0]}")
  
  
  
  # Ask for another card
  while another_card:
    if input("Type 'y' to get another card, type 'n' to pass: ") == 'n':
      another_card = False
      
      while computer_score < 17:
        new_card = random.choice(cards)
        computer_cards.append(new_card)
        computer_score += new_card
  
      while computer_score < user_score:
        new_card = random.choice(cards)
        computer_cards.append(new_card)
        computer_score += new_card
        
      if computer_score >= user_score:
        if computer_score > 21:
          print(f"Your card: {user_cards}, current score: {user_score}")
          print(f"Computer card: {computer_cards}, current score: {computer_score}")
          print("You win!")
        elif computer_score == user_score:
          print(f"Your card: {user_cards}, current score: {user_score}")
          print(f"Computer card: {computer_cards}, current score: {computer_score}")
          print("Draw!")
        else:
          print(f"Your card: {user_cards}, current score: {user_score}")
          print(f"Computer card: {computer_cards}, current score: {computer_score}")
          print("You lose!")
  
          
    else:
      new_card = random.choice(cards)
      user_cards.append(new_card)
      user_score += new_card
      
      if user_score > 21:
        another_card = False
        print(f"Your card: {user_cards}, current score: {user_score}")
        print(f"Computer card: {computer_cards}, current score: {computer_score}")
        print("You lose!")
      else:
        print(f"Your card: {user_cards}, current score: {user_score}")