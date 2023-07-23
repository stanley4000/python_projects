from game_data import data
from art import *
import random

current_score = 0
def play():
  #choose two random items
  global current_score
  global choice_a
  global choice_b
  if current_score == 0:
    random_items = random.sample(data, 2)
    choice_a = random_items[0]
    choice_b = random_items[1]
    
  else:
    choice_a = choice_b
    choice_b = random.choice(data)
  #this returns two dictionaries in a list [A, B]
  
  print(logo)
  #print current score
  print(f"Current score: {current_score}")
  #print choice a; vs; choice b
  print(f"A: {choice_a['name']}, {choice_a['description']} from {choice_a['country']}." )
  print(vs)
  print(f"B: {choice_b['name']}, {choice_b['description']} from {choice_b['country']}.")
  #player chooses
  player_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
  if player_choice == 'a':
    player_choice = choice_a['follower_count']
    cpu_choice = choice_b['follower_count']
  else:
    player_choice = choice_b['follower_count']
    cpu_choice = choice_a['follower_count']
  #compare choices
  if player_choice >= cpu_choice:
    current_score += 1
    print("You are right!")
    play() 
  else:
    print(f"Sorry, that's wrong. Final score: {current_score}")
  
play()

