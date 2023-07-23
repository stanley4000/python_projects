#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from random import randint
gameover = False 
i = 0
while gameover == False:
    while i == 0:    
        mode = input("Do you want to play easy or hard mode? (Type 'easy' or 'hard'): ").lower()
        if mode == "easy":
            i = 9
        elif mode == "hard":
            i = 4
        else:
            mode = input("I did not understand you. Type 'easy' or 'hard': ").lower()

    number = randint(1, 100)

    guess = int(input("I'm thinking of a number between 1 and 100. Guess the number: "))

    while i > 0:
#NOte: this could be called as a function
        if guess == number:
            print(f"You guessed it! The number is {number}")
            gameover = True
            break
            
        if guess < number:
            i -= 1
            guess = int(input("Too low. Guess again: "))
            
        if guess > number:
            i -= 1
            guess = int(input("Too high. Try again: "))
            

    if i == 0:
        print("You have no more tries. You lose!")
        gameover = True

    if gameover == True:
        if input("Do you want to play again? Enter y/n: ").lower() == "y":
            i = 0
            gameover = False
        else:
            print("Goodbye.")
            exit()