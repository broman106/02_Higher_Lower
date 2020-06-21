# HL component 9b - End game stats

# to do
# set up game play list with each rounds results
# set up average, best and worst scores (see 09b stats_ experiment)


SECRET = 7
GUESSES_ALLOWED = 4
round = int(input("how many rounds? "))    # replace with int check
game_stats = []

num_won = 0
rounds_played = 0

# main routine starts here

# Start of round
while rounds_played < round:
    guess = ""
    guesses_left = GUESSES_ALLOWED

    print()

    rounds_played += 1
    print("Round {}".format(rounds_played ))

    while guess != SECRET and guesses_left >= 1:

        guess = int (input("guess: "))  # replace this with function call in due count
        guesses_left -= 1

        if guesses_left >= 1:

            if guess < SECRET:
                print("too high, try a lower number. guesses left: {}".format(guesses_left))

            elif guess > SECRET:
                print("too low, try a higher number. guesses left: {}".format(guesses_left))
            else:
                if guess < SECRET:
                    print("too high!")
                elif guess > SECRET:
                    print("too low!")

            if guess == SECRET:
                if guesses_left ==GUESSES_ALLOWED - 1:
                    print("mean as ko! you got it one guess")
                else:
                    print("well done, oyu got it in {} guesses".format(GUESSES_ALLOWED - guesses_left))
                    guesses_left -= 1 # penalty point for losing

                # update number won
                num_won += 1

print()
print("****** Game Stats ******")
print("Games Won: {}".format(num_won))
print("Games Lost: {}".format(rounds_played - num_won))
print("Games Played: {}".format(rounds_played))
print()


