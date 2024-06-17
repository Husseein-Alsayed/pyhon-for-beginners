# Uncomment the following line to enable master password prompt
# master_pass = input("Please enter your master password:\n")

# Function to add a new username and password to the credentials file
def add():
    # Prompt user for username
    user_name = input("Please enter your username: ")
    # Prompt user for password
    password = input("Please enter your password: ")
    # Open the credentials file in append mode and write the username and password
    with open('credentials.txt', 'a') as f:
        f.write(user_name + "|" + password + "\n")

# Function to view all stored usernames and passwords
def view():
    try:
        # Open the credentials file in read mode
        with open('credentials.txt', 'r') as f:
            # Read each line in the file
            for line in f.readlines():
                # Strip any leading/trailing whitespace characters
                data = line.strip()
                # Split the line into username and password
                user, passw = data.split("|")
                # Print the username and password
                print("Username:", user, ",", "Password:", passw)
    except FileNotFoundError:
        # If the file does not exist, print an error message and quit
        print("The file you are looking for does not exist!")
        quit()

# Main loop to prompt user for mode and call the corresponding function
while True:
    # Prompt user to enter mode (view or add)
    mode = input("Please enter your mode (view/add): ").lower()
    # If user enters 'q', break the loop and exit
    if mode == "q":
        break
    # If mode is 'view', call the view function
    if mode == "view":
        view()
    # If mode is 'add', call the add function
    elif mode == "add":
        add()
    # If user enters an invalid mode, print an error message
    else:
        print("Enter a valid value.")
        continue
