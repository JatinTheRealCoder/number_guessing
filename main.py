import random  # Importing the random module to generate a random number

# Generate a random number between 1 and 100
random_int = random.randint(1, 100)

try:
    # Allow the user to guess up to 5 times
    for i in range(1, 6):
        print("Guess the number between 1 and 100. You have", 6 - i, "attempts left.")

        # Take user input and convert it to an integer
        num = int(input("Enter the number: "))

        # Function to check the guess
        def guess_number(num):
            if num < random_int:
                print("Your guess is too low")
            elif num > random_int:
                print("Your guess is too high")
            else:
                print("Congratulations! You guessed the number correctly.")

        guess_number(num)

    # If the user didn't guess correctly in 5 attempts, show failure message
    print("You failed as a gamer! The number was:", random_int)

# Catch any error such as invalid (non-integer) input
except Exception as e:
    print("Please enter a valid number.", e)
