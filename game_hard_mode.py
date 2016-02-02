import random

print("Pick a number between 1 and 99 and I will try to guess.")
print("Tell me if I'm too (L)ow, too (H)igh, or if (Y)es I got it!")


hi_guess = 99
lo_guess = 1
comp_guesses = []
guess_count = 5

while guess_count > 0:

    guess = random.randint(lo_guess, hi_guess)

    if guess not in comp_guesses:
        user_response = input("Is your secret number {}?".format(guess))
        if user_response.lower() == "h":
            guess_count -= 1
            comp_guesses.append(guess)
            hi_guess = guess
        elif user_response.lower() == "l":
            guess_count -= 1
            comp_guesses.append(guess)
            lo_guess = guess
        elif user_response.lower() == "y":
            print("Hooray I'm smart!")
            break
        else:
            print("Please respond with an 'L','H' or 'Y'")


