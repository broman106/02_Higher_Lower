import random

# Number checking function goes here
def intcheck(question, low=None, high=None):

    #sets up error messages
    if low is not None and high is not None:
            error = "Please enter an integer between {} and {} " \
                    "(inclusive)".format(low,high)
    elif low is not None and high is None:
        error = "Please enter an integer that is more than or " \
                "equal to {}".format(low)
    elif low is None and high is not None:
        error = "please  enter an integer that is less tha or " \
                "equal to {}".format(high)
    else:
        error = "please enter an integer"

    while True:

         try:

            response = int(input(question))

            # Checks response is not too low
            if low is not None and response < low:
                print(error)
                continue

            # Checks response is not too high
            if high is not None and response > high:
                print(error)
                continue

            return response

         except ValueError:
            print(error)
            continue

# Main routine goes here

# Get user input...
lowest = intcheck("Low Number: ")
highest = intcheck("High Number: ", lowest + 1)
rounds = intcheck("Rounds: ", 1)
guesses_allowed = intcheck("How many guesses do you want? ", 1)

secret = random.randint(lowest, highest)

num_won = 0
rounds_played = 0

while rounds_played < rounds:
    guess = ""
    guesses_left = guesses_allowed

    while guess != secret and guesses_left >= 1:

        guess = int(input("guess: "))  # replace this with function call in due course
        guesses_left -= 1

        # if guessess are left, tell user to try again...
        if guesses_left >= 1:

            # too low
            if guess < secret:
                print("too low, try a higher number. guesses left: {}" .format(guesses_left))
            # too high
            elif guess > secret:
                print("too low, try a higher number.  guesses left: {}".format(guesses_left))

        # If there are not more guesses, just give result
        else:
            if guess < secret:
                print("too low")
            elif guess > secret:
                print("too high")

    # correct guess :)
    if guess == secret:
        if guesses_left == guesses_allowed - 1:
            print("amazing! you got it in one guess")
        else:
            print("well done, you got it in {} guesses".format(guesses_allowed - guesses_left))
            num_won += 1
    else:
        print("sorry - you lose this round as you have run out of guesses")

    print("won: {} \t | \t lost:{}".format(num_won, rounds_played - num_won + 1))
    rounds_played += 1