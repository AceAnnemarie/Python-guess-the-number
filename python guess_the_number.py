Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
... 
... def guess_the_number():
...     # Generate a random number between 1 and 100
...     number_to_guess = random.randint(1, 100)
...     attempts = 0
...     guessed_correctly = False
...     
...     print("Welcome to 'Guess the Number'!")
...     print("I have selected a number between 1 and 100.")
...     
...     while not guessed_correctly:
...         try:
...             # Ask the player to enter their guess
...             guess = int(input("Enter your guess: "))
...             attempts += 1
...             
...             if guess < number_to_guess:
...                 print("Too low! Try again.")
...             elif guess > number_to_guess:
...                 print("Too high! Try again.")
...             else:
...                 print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
...                 guessed_correctly = True
...         except ValueError:
...             print("Please enter a valid integer.")
...     
... if __name__ == "__main__":
...     guess_the_number()
