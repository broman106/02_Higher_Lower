# HL component 3 - compares user with secert number

# To Do
# set up number of guesses
# count # of guesses
# if user runs out of guesses, print 'you lose'
# if user guesses the secret number within number of guesses print'well done'

SECRET = 7
GUESSES_ALLOWED = 4

#initialise variables
already_guessed = []
guesses_left = GUESSES_ALLOWED
num_won = 0

guess = ""

# start game
while guess != SECRET and guesses_left >= 1:

    guess = int(input("Guess "))    # replace this with call in due course

    # checks that guess is not a duplicate
    if guess in already_guessed:
        already_error = "You already guessed that number! Please try again.  " \
                        "You *Still* have {} guesses left".format(guesses_left)
        print(already_error)
        continue

    guesses_left -= 1
    # add guess to list of numbers already guessed
    already_guessed.append(guess)

    if guesses_left >= 1:

        if guess < SECRET:
            print("Too low, try a higher number. Guesses left; {}".format(guesses_left))

        elif guess > SECRET:
            print("too high,try a lower number. gueses left: {}".format(guesses_left))

    else:
        if guess > SECRET:
            print("Too low!")
        elif guess > SECRET:
            print("Too high!")

if guess == SECRET:
    if guesses_left == GUESSES_ALLOWED - 1:
        print("Amazing! you got  it in one guess")
    else:
        print("well done, you got it in {} guesses".format(len(already_guessed)))
    num_won += 1
else:
    print("Sorry - youlose this round as you have run out of guesses")
    