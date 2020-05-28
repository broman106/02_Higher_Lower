# HL component 3 - compares user guess with secret number

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


secret = random.randint(lowest, highest)

guess = ""

while guess != secret:

    guess = intcheck("Guess: ", lowest, highest)

    if guess < secret:
        print("Too high, try a lower number")
    elif guess > secret:
        print("Too low, try a higher number")
    else:
        print("Well done! You guessed the secret number")
