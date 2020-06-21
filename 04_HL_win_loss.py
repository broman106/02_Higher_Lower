# HL component 3 - compares user with secert number

# To Do
# set up number of guesses
# count # of guesses
# if user runs out of guesses, print 'you lose'
# if user guesses the secret number within number of guesses print'well done'

secret = 7
GUESSES_ALLOWED = 4

#initialise variables
already_guessed = []
guesses_left = GUESSES_ALLOWED
num_won = 0

guess = ""

# start game
while guess != secret and guesses_left >= 1:

    guess = int(input("Guess "))    # replace this with call in due course

    # checks that guess is not a duplicate
    if guess in already_guessed:
        already_error = "You already guessed that number! Please try again.  " \
                        "You *Still* have {} guesses left".format(guesses_left)
        print(already_error)
        continue

    guesses_left -= 1
    already_guessed.append(guess)

    if guess == secret:
        print("You win")
    else:
        # should be a higher / lower message
        print("Nope, try again.  you have {} guesses left".format(guesses_left))

    if guesses_left == 0:
        print("You have run out of guess <you lose>")

