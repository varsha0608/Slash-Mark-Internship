#Features:
 -> Random Number Generation: The game will randomly pick a number within a predefined range (e.g,1 to 200).
 -> User Input: Players will be able to guess the hidden number by entering their guesses.
 -> Number of Attempts: There will be a limit on the number of guesses allowed (e.g,6 attempts).
 -> Win/Lose Condition: The game will determine if the player successfully guesses the number within the allowed attempts.


# Code in Words:
  -> It uses the random.randint(1, 200) function to select a random integer between 1 and 200 (both inclusive). This becomes your target number, stored secretly within the class as self.number.
  -> self.max_guesses and sets it to 6. This determines the maximum number of attempts you'll have to guess the hidden number.
  -> self.intro_message: Welcomes you and introduces the game.
  -> self.win_message: A celebratory message congratulating you on guessing the number.
  -> self.lose_message: A message revealing the hidden number if you couldn't guess it within the allowed attempts.






   import random
import time


class NumberGuessingGame:
    def __init__(self):
        self.number = random.randint(1, 200)
        self.max_guesses = 6
        self.intro_message = (
            "Welcome to the Number Guessing Game!\n"
            "I'm thinking of a number between 1 and 200.\n"
            "Try to guess it!"
        )
        self.win_message = "Congratulations! You guessed the number {number} in {guesses} guesses."
        self.lose_message = "Sorry, you didn't guess the number. It was {number}."

    def play(self):
        print(self.intro_message)
        guesses_taken = 0
        while guesses_taken < self.max_guesses:
            guess = self.get_valid_guess()
            guesses_taken += 1
            if self.check_guess(guess):
                break
            self.provide_hint(guess)

        self.reveal_answer(guesses_taken)

    def get_valid_guess(self):
        while True:
            guess_str = input("Enter your guess: ")
            try:
                guess = int(guess_str)
                if 1 <= guess <= 200:
                    return guess
                else:
                    print("Please enter a number between 1 and 200.")
            except ValueError:
                print("Please enter a valid number.")

    def check_guess(self, guess):
        return guess == self.number

    def provide_hint(self, guess):
        if guess < self.number:
            print("Your guess is too low. Try again!")
        else:
            print("Your guess is too high. Try again!")

    def reveal_answer(self, guesses_taken):
        if guesses_taken < self.max_guesses:
            print(self.win_message.format(number=self.number, guesses=guesses_taken))
        else:
            print(self.lose_message.format(number=self.number))

    def play_again(self):
        while True:
            again = input("Do you want to play again? (yes/no): ").lower()
            if again in ("yes", "no", "y", "n"):
                return again
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")


def main():
    game = NumberGuessingGame()
    while True:
        game.play()
        if game.play_again() != "yes":
            print("Thank you for playing!")
            break


if __name__ == "__main__":
    main()
