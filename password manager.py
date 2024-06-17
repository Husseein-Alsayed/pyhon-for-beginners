
# master_pass = input("Please enter your master password:\n")


def add():
    user_name = input("pleas enter your username:")
    password = input("Please enter your password:")
    with open('credentials.txt', 'a') as f:
        f.write(user_name + "|" + password + "\n")


def view():

 try:
    with open('credentials.txt', 'r') as f:
        for line in f.readlines():
            data = line.strip()
            user, passw = data.split("|")
            print("username:", user, ",", "password:", passw)
 except FileNotFoundError:
     print("the file you are looking for is not exist!")
     quit()

while True:
    mode = input("please enter your mode (view/add):").lower()
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("enter a valid value.")
        continue
