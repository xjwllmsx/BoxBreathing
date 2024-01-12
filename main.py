# Import exit() from sys module
from sys import exit
# Import sleep() from time module
from time import sleep
# Import clear() from replit module
from replit import clear


# Delay function
def delay():
  """Adds a delay of 1 second before the next out"""
  sleep(1)


# Breath In function
def breath_in():
  """Prints prompts for user to begin breathing in for 4 seconds"""
  clear()
  print("Breath in...")
  delay()
  print("4")
  delay()
  print("3")
  delay()
  print("2")
  delay()
  print("1")
  delay()
  print("0")


# Breath Out function
def breath_out():
  """Prints prompts for user to begin breathing out for 4 seconds"""
  clear()
  print("Breath out...")
  delay()
  print("4")
  delay()
  print("3")
  delay()
  print("2")
  delay()
  print("1")
  delay()
  print("0")


# Hold Breath function
def hold_breath():
  """Prints prompts for user to hold their breath for 4 seconds"""
  clear()
  print("Hold...")
  delay()
  print("4")
  delay()
  print("3")
  delay()
  print("2")
  delay()
  print("1")
  delay()
  print("0")


# Countdown function
def countdown():
  """Prints a countdown for the user"""
  clear()
  print("We'll begin in...")
  delay()
  print("5")
  delay()
  print("4")
  delay()
  print("3")
  delay()
  print("2")
  delay()
  print("1")
  delay()
  print("Let's begin!")


# Round of Breath function
def round_of_breath():
  """The function completes 1 round of breathing"""
  delay()
  breath_in()
  delay()
  hold_breath()
  delay()
  breath_out()
  delay()
  hold_breath()
  delay()


# Ask for Rounds function
def ask_for_rounds():
  """This function asks the user to input their desired number of rounds, and returns the input"""

  # Ask user to input their desired number of rounds
  print('How many rounds of breathing would you like to do?')
  user_input = input(
      'Enter a number between 1 and 5, or type "0" to exit the program: ')

  # Run if user_input contains only numbers
  if user_input.isnumeric():
    # If user_input is a number, convert from string to int
    desired_number_of_rounds = int(user_input)

    # Run if user inputs 0
    if desired_number_of_rounds == 0:
      print('Take care!')
      exit()

    # Run if user input is greater than 10
    elif desired_number_of_rounds > 5:
      print("Try a smaller number, preferably between 1 and 5")
      return ask_for_rounds()

    # Run if user inputs a number greater than 1
    elif desired_number_of_rounds > 1:
      print(
          f"Excellent! We'll do {desired_number_of_rounds} rounds of box breathing."
      )
    # Run if user inputs 1
    else:
      print(
          f"Excellent! We'll do {desired_number_of_rounds} round of box breathing."
      )

    # Return the user input
    return desired_number_of_rounds

  else:
    # Checks if user_input is a negative number or not a number
    while not user_input.isnumeric():
      print("Invalid input")
      return ask_for_rounds()


# Greet the user
print("Welcome to the Box Breathing program!")
# Ask for number of rounds
num_of_rounds = ask_for_rounds()
# Loop while the number of rounds is greater than 0
while num_of_rounds > 0:
  counter = 0
  # Ask the user if they are ready to begin their breathing exercise
  ready_to_start = input('Type "start" when you are ready to begin: ').lower()
  # Start the breathing exercise if the user inputs 'start'
  if ready_to_start == 'start':
    # Display the countdown
    countdown()
    # Loop until number of rounds is equal to 0
    while num_of_rounds != 0:
      # Call round of breath function
      round_of_breath()
      # Subtract 1 from number of rounds
      num_of_rounds -= 1
      # Add 1 to counter
      counter += 1
    # Clear the console
    clear()
    # Print if the counter is greater than 1
    if counter > 1:
      print(f"Great work! You completed {counter} rounds of box breathing.")
    # Print if the counter is not 1
    else:
      print(f"Great job! You completed {counter} round of box breathing.")
    # Ask the user if they would like to continue with their breathing exercises
    continue_breathing = input(
        'Would you like to do additional rounds of breathing? Type "yes" or "no": '
    ).lower()
    # Clear the console and ask for number of rounds if the user wants to continue
    if continue_breathing == 'yes':
      clear()
      num_of_rounds = ask_for_rounds()
    # End the program if the user does not want to continue
    elif continue_breathing == 'no':
      print('Enjoy the rest of your day. Namaste!')
      exit()
    # Print if the user enters an invalid input
    else:
      print('Invalid input.')
