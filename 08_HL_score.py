# HL component 8 - set up score mechancis

# to do
# set up round and win counter
# update feedback statements


SECRET = 7
GUESSES_ALLOWED = 4
rounds = 3

num_won = 0
rounds_played = 0

while rounds_played < rounds:
    guess = ""
    guesses_left = GUESSES_ALLOWED

    while guess != SECRET and guesses_left >= 1:

        guess = int(input("guess: "))  # replace this with function call in due course
        guesses_left -= 1

        # if guessess are left, tell user to try again...
        if guesses_left >= 1:

            # too low
            if guess < SECRET:
                print("too low, try a higher number. guesses left: {}" .format(guesses_left))
            # too high
            elif guess > SECRET:
                print("too low, try a higher number.  guesses left: {}".format(guesses_left))

        # If there are not more guesses, just give result
        else:
            if guess < SECRET:
                print("too low")
            elif guess > SECRET:
                print("too high")

    # correct guess :)
    if guess == SECRET:
        if guesses_left == GUESSES_ALLOWED - 1:
            print("amazing! you got it in one guess")
        else:
            print("well done, you got it in {} guesses".format(GUESSES_ALLOWED - guesses_left))
            num_won += 1
    else:
        print("sorry - you lose this round as you have run out of guesses")

    print("won: {} \t | \t lost:{}".format(num_won, rounds_played - num_won + 1))
    rounds_played += 1