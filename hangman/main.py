import random
from hangman_art import *
from hangman_words import word_list
should_continue = True
while should_continue == True:
    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)
    wrong_choices = []
    end_of_game = False
    lives = 6
    print(logo)
    print(stages[lives])
    display = []
    for _ in range(word_length):
        display += "_"
    print(f"{' '.join(display)}")

    while not end_of_game:
        guess = input("Guess a letter: ").lower()
        if guess in display:
            print(f"You already chose {guess}.\n{' '.join(display)}")
            guess = input("Guess another letter: ").lower()

        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

        if guess not in chosen_word:
            print(f"There is no '{guess}' in the word. You lose a life!")
            lives -= 1
            wrong_choices += guess
            if lives == 0:
                end_of_game = True
                print("You lose!")
                print(stages[lives])
                print(f"The word was {chosen_word}")
                if input("Enter 'y' if you want to play again: ").lower() == "y":
                    continue
                else:
                    should_continue = False
                    print("Goodbye.")

        if "_" not in display:
            end_of_game = True
            print(f"The word is {chosen_word}")
            print("You win!")
            if input("Enter 'y' if you want to play again: ").lower() == "y":
                continue
            else:
                should_continue = False
                print("Goodbye.")
        print(stages[lives])
        if end_of_game == False:
            print(f"{' '.join(display)}")
            print(f"(Wrong choices: {' '.join(wrong_choices)})")