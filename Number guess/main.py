from art import logo
from random import randint

EASY_DIFF = 10
HARD_DIFF = 5
turns = 0

def chosen_diff():
  diff = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if diff == 'easy':
    return EASY_DIFF
  else:
    return HARD_DIFF

def check_answer(guess, answer, turns):
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print("You guessed the number. Congratulations!")

def game():
  print(logo)
  print("""Welcome to the Number Guessing game!
          I'm thinking of a number between 1 and 100.""")
  answer = randint(1, 101)

  turns = chosen_diff()
  guess = 0

  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number")   
    guess = int(input("Make a guess:"))
    
    turns = check_answer(guess, answer, turns)
    continue
        
    print("You've run out of attempts to guess. You lose.")
    
game()





  


  

  

  








