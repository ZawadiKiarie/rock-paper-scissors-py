import random

#r>s>p>r

def play():
  user = input("Choose rock, paper or scissors: ").lower()
  computer = random.choice(['rock', 'paper', 'scissors'])

  if computer == user:
    print(f"Computer chose {computer}. It's a tie")
  elif isWin(user, computer):
    print(f"Computer chose {computer}. {user} beats {computer}. You win!")
  else:
    print(f"Computer chose {computer}. {computer} beats {user}. You Lost!")
  

def isWin(player, opponent):
  if (player == 'rock' and opponent == 'scissors') or (player == 'scissors' and opponent == 'paper') or (player == 'paper' and opponent == 'rock'):
    return True
  
play()