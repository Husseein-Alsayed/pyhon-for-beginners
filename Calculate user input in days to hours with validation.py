# Constants for time calculations
calculation_to_hours = 24  # 1 day = 24 hours
calculation_to_minutes = 24 * 60  # 1 day = 1440 minutes

# Function to convert days to hours
def days_to_units(number_of_days):
    return f"{calculation_to_hours * number_of_days}"  # Return the total hours for the given number of days

# Function to validate user input and print the result
def validation():
    try:
        # Convert the current element to an integer
        user_input_int = int(number_of_days_element)

        # Check if the number is positive
        if user_input_int > 0:
            # Calculate the hours and print the result
            my_value = days_to_units(user_input_int)
            print(f"{user_input_int} days are {my_value} hours")
        elif user_input_int == 0:
            # Handle the case where the input is zero
            print(f"Your input is ({user_input}) which is not valid as a correct value of days!!")
        else:
            # Handle negative numbers
            print("Negative number! Really, man?")
    except ValueError:
        # Handle invalid input that cannot be converted to an integer
        print(f"Your input is ({user_input}) which is not valid as a correct value of days!!")

# Main loop to keep the program running until the user types 'exit'
user_input = ""

while user_input != "exit":
    # Prompt the user for input
    user_input = input("Enter your number to be calculated OR type 'exit' to quit the program:\n")
    
    # Split the user input by spaces and process each element
    for number_of_days_element in user_input.split():
        validation()
