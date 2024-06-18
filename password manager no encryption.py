# Prompt the user to enter the master password
master_pass = input("please enter your master password:")

# Define the function to add new credentials
def add():
    # Prompt the user to enter a username and password
    username = input("please enter the username:").lower()
    password = input("please enter the password:").lower()
    # Open the credentials file in append mode and write the new credentials
    with open('credentials.txt', 'a') as f:
        f.write(username + ',' + password + "\n")

# Define the function to view stored credentials
def view():
    try:
        # Open the credentials file in read mode
        with open('credentials.txt', 'r') as f:
            for line in f:
                # Strip any whitespace from the line and split it into username and password
                data = line.strip()
                user, passw = data.split(",")
                # Print the username and password
                print("Username:" + user, ",", "Password:" + passw)
    except:
        # Handle the case where the file is not available
        print("file is not available.")
        user_action()

# Define the main function for user actions
def user_action():
    while True:
        try:
            # Prompt the user to choose an action: add, view, or quit
            ask_for_option = input("Please enter add to add, view to view and q for quit:").lower()
            if ask_for_option == "q":
                # Exit the program if the user chooses to quit
                quit()
            elif ask_for_option == "add":
                # Call the add function if the user chooses to add credentials
                add()
            elif ask_for_option == "view":
                # Call the view function if the user chooses to view credentials
                view()
            else:
                # Prompt the user to enter a valid value if the input is invalid
                print("Please enter a valid value.")
                continue
        except:
            # Exit the program in case of an unexpected error
            quit()

# Start the user action function
user_action()
