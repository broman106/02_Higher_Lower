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


def statement_decorator(statement, decoration):
    print(decoration * len(statement))
    print(statement)
    print(decoration * len(statement))
    return ""

# Main routine goes here

# Get user input...
lowest = intcheck("Low Number: ")
highest = intcheck("High Number: ", lowest + 1)
rounds = intcheck("Rounds: ", 1)




# Start of game
rounds_played = 0
num_won = 0
GUESSES_ALLOWED = 4

# Empty list to hold game history
history =[]

# Start of round
while rounds_played < rounds:
    secret = random.randint(lowest, highest)
    print(secret)

    guess = ""
    guesses_left = GUESSES_ALLOWED

    print()

    rounds_played += 1
    print("Round {}".format(rounds_played ))

    while guess != secret and guesses_left >= 1:

        guess = intcheck("guess: ", lowest, highest)  # replace this with function call in due count
        guesses_left -= 1

        if guesses_left >= 1:

            if guess > secret:
                feedback = "too high, try a lower number. guesses left: {}".format(guesses_left)
                statement_decorator(feedback, "v")

            elif guess < secret:
                feedback = "too low, try a higher number. guesses left: {}".format(guesses_left)
                statement_decorator(feedback, "^")
            else:
                if guess > secret:
                    statement_decorator("too high!", "v")
                elif guess < secret:
                    statement_decorator("too low!", "^")

                # Add result to game history list
                    history.append("Round {}: Lost".format(rounds_played))

            if guess == secret:
                if guesses_left ==GUESSES_ALLOWED - 1:
                    print("****mean as ko! you got it in one guess my g****")
                else:
                    print("well done my bro, you got it in {} guesses".format(GUESSES_ALLOWED - guesses_left))
                    guesses_left -= 1 # penalty point for losing

                history.append("Round {}: Won".format(rounds_played))

                # update number won
                num_won += 1

print()
print("****** Game Stats ******")
print("Games Won: {}".format(num_won))
print("Games Lost: {}".format(rounds_played - num_won))
print("Games Played: {}".format(rounds_played))
print()

print("***** Game History ******")

for item in history:
    print(item)

print()
statement_decorator("We are done", "!")