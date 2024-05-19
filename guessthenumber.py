import random

def play_guessing_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    max_attempts = 10  # You can adjust this as needed

    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and 100. Can you guess it?")

    for attempt in range(1, max_attempts + 1):
        guess = int(input(f"Attempt {attempt}/{max_attempts}: Enter your guess: "))

        if guess < secret_number:
            print("Too low! Try a higher number.")
        elif guess > secret_number:
            print("Too high! Try a lower number.")
        else:
            print(f"Congratulations! You guessed it right. The secret number was {secret_number}.")
            break
    else:
        print(f"Sorry, you've reached the maximum number of attempts. The secret number was {secret_number}.")

if __name__ == "__main__":
    play_guessing_game()