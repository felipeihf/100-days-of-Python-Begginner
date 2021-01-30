import art
import random
import game_data
from replit import clear

print(art.logo)

contender_1 = random.choice(game_data.data)
contender_2 = random.choice(game_data.data)

SCORE = 0
streak = True

def assign_profiles():

  print(f"Compare A: {contender_1['name']}, a {contender_1['description']}, from {contender_1['country']}.")

  print(art.vs)

  print(f"Against B: {contender_2['name']}, a {contender_2['description']}, from {contender_2['country']}.")


def compare_followers():
  if contender_1['follower_count'] > contender_2['follower_count']:
    return "A"
  elif contender_1['follower_count'] < contender_2['follower_count']:
    return "B"
  else:
    pass

def switch_contender():
  if contender_1['follower_count'] > contender_2['follower_count']:
    return contender_1
  else:
    return contender_2

while streak:
  assign_profiles()
  if input("Who has more followers? Type 'A' or 'B' :") == compare_followers():
    SCORE += 1
    clear()
    print(art.logo)
    print(f"Correct! Current score: {SCORE}")
    contender_1 = switch_contender()
    contender_2 = random.choice(game_data.data)
  else:
    streak = False
    clear()
    print(f"You lose! Final score: {SCORE}")





      



