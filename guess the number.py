import random
Generated_number = random.randint(0, 10)
print(Generated_number)
user_input = Generated_number + 1

def chek():
 try:
  user_input_int = int(user_input)
  if user_input_int == Generated_number:
      print("correct_if")
      quit()
  elif user_input_int > Generated_number:
      print("Smaller")
  else: #user_input_int < Generated_number:
      print("Bigger")

 except:
    print("fuck you!")
    quit()

while user_input != Generated_number:
    user_input = input("enter your number:\n")

    chek()
