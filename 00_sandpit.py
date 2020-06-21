def num_check(question):

    valid = False
    while not valid:

        try:
            response = int(input(question))

            # check number is more than zero
            if response <= 0:
                print("Please enter an integer that is  more than zero")
            else:
                return response

        except ValueError:
            print("Please enter an integer")
            print()

# Ask user for two best numbers
best_num = num_check("What is your favourite number? ")
next_num = num_check("What is your next best number? ")

print(best_num)
print(next_num)