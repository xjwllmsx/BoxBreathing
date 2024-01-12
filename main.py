# Import exit() from sys module
from sys import exit
# Import sleep() from time module
from time import sleep
# Import clear() from replit module
from replit import clear
# Import all functions from howManyRounds module
from howManyRounds import ask_for_rounds
# Import round_of_breath from breathInAndOut module
from breathInAndOut import round_of_breath
# Import countdown from countdown module
from countdown import countdown


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
