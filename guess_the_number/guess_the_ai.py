from random import randint

gameover = False
max_guesses = 5

while not gameover:
    mode = input("Do you want to play easy or hard mode? (Type 'easy' or 'hard'): ").lower()

    if mode == "easy":
        max_guesses = 10
    elif mode == "hard":
        max_guesses = 5
    else:
        print("I did not understand you. Type 'easy' or 'hard'.")
        continue

    number = randint(1, 100)

    for _ in range(max_guesses):
        guess = int(input("I'm thinking of a number between 1 and 100. Guess the number: "))

        if guess == number:
            print(f"You guessed it! The number is {number}")
            gameover = True
            break

        if guess < number:
            print("Too low. Guess again.")
        else:
            print("Too high. Guess again.")

    if not gameover:
        print("You have no more tries. You lose!")

    if input("Do you want to play again? Enter y/n: ").lower() != "y":
        print("Goodbye.")
        break
