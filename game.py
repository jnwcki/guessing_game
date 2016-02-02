
import random

def guessing_game():

    print("I'm thinking of a number between 1 and 99."
          "You have five guesses and I'll let you know if it's too high or low.")
    secret_num = random.randint(1, 99)
    guess_count = 5
    for _ in range(guess_count):
        try:
            guess_count -= 1
            guess = int(input("> "))

            if abs(guess - secret_num) in range(1, 10):
                print("You are close!")
            if guess < secret_num:
                print("That guess was too low. You have {} tries left.".format(guess_count))
            elif guess > secret_num:
                print("That guess was too high. You have {} tries left.".format(guess_count))
            elif guess == secret_num:
                print("You guessed it! You had {} tries left.".format(guess_count))
                break
        except ValueError:
            if guess_count > 0:
                print("That is not a number. Try again.")
            else:
                print("You are being silly.")

guessing_game()


