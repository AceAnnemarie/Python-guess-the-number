import random

def guess_the_number():
    """
    A simple number guessing game where the player tries to guess a randomly selected number between 1 and 100.
    """
    while True:
        number_to_guess = random.randint(1, 10)
        attempts = 0
        guessed_correctly = False
        
        print("Welcome to 'Guess the Number'!")
        print("I have selected a number between 1 and 10.")
        
        while not guessed_correctly:
            try:
                # Ask the player to enter their guess
                guess = int(input("Enter your guess: "))
                attempts += 1
                
                if guess < number_to_guess:
                    print("Too low! Try again.")
                elif guess > number_to_guess:
                    print("Too high! Try again.")
                else:
                    print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
                    guessed_correctly = True
            except ValueError:
                print("Please enter a valid integer.")
        
        # Ask if the player wants to play again
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    guess_the_number()
