import random

# Function to check the user's input against the generated number
def check(user_input, generated_number):
    try:
        # Convert user input to integer
        user_input_int = int(user_input)
        
        # Check if the guess is correct
        if user_input_int == generated_number:
            print("Correct! You've guessed the number.")
            return True
        
        # Give feedback if the guess is too high
        elif user_input_int > generated_number:
            print("Try a smaller number.")
        
        # Give feedback if the guess is too low
        else:
            print("Try a bigger number.")
        
        # Return False to indicate the game should continue
        return False
    
    # Handle the case where user input is not a valid integer
    except ValueError:
        print("Please enter a valid integer.")
        return False

# Main function to run the game
def main():
    # Generate a random number between 0 and 10
    generated_number = random.randint(0, 10)
    
    # Welcome message and instructions
    print("Welcome to the number guessing game!")
    print("I've selected a number between 0 and 10. Try to guess it!")

    # Loop until the user guesses the correct number
    while True:
        # Prompt user for their guess
        user_input = input("Enter your guess:\n")
        
        # Check the user's guess and break the loop if correct
        if check(user_input, generated_number):
            break

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
