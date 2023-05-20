from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)

bid = {}
other_user = True

while other_user:
  name = input("What's your name?")
  price = int(input("What's your bid?"))
  
  bid[name] = price
  
  answer = input("Other user? (yes or no)")
  if answer == "no":
    other_user = False
    best = 0
    winner = ""
    for user in bid:
      if bid[user] > best:
        best = bid[user]
        winner = user
    print(f"Winner is: {winner}")
  else:
    clear()