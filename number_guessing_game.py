# Number guessing name
import random

lowest_num = 1
highest_num = 100
number = random.randint(lowest_num, highest_num)
running = True

# Initialize the game
while running:
    print("--- WELCOME TO THE NUMBER GUESSING NAME ---")
    print("I'm thinking of a number between 1 and 100.\n")
    print("Please Select the difficulty level: ")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")

# Creates new variables and resets them every new round
    difficulty = None
    chances = 0
    guess = None
    attempts = 0

# Makes sure the user is typing one of the options
    while difficulty not in range(1,4):
        difficulty = int(input("Enter your choice: "))
# Collects and sets the difficulty level
        if difficulty == 1:
            chances = 10
            print("Great! You have selected the Easy difficulty level.")
        elif difficulty == 2:
            chances = 5
            print("Great! You have selected the Medium difficulty level.")
        elif difficulty == 3:
            chances = 3
            print("Great! You have selected the Hard difficulty level.")

# Asks for a guess, and ends when there are not more chances
    while chances != 0:
        guess = int(input("Enter your guess: "))
        chances -= 1
        attempts += 1
        if guess < lowest_num and not 0 or guess > highest_num:
            print("Invalid choice, try a number between 1 and 100.")
        elif guess < number:
            print(f"Incorrect, the number is greater than {guess}")
            print(f"Remaining chances: {chances}")
        elif guess > number:
            print(f"Incorrect the number is less than {guess}")
            print(f"Remaining chances: {chances}")
        elif guess == number:
            print(f"Congrats! You guessed the number in {attempts} attempts.")
    else: # Asks if user wants to play again
        print("Sorry, you have run out of chances.")
        if not input("Wanna play again (y/n): ").lower() == "y":
            running = False
            print("Thanks for playing! Bye now")




















