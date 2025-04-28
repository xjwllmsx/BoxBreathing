from .clear import clear

def process_user_input(user_input):
  """Using conditional statements, this function will generate the proper output based on the user's input"""
  # If user_input is a number, convert from string to int
  desired_number_of_rounds = int(user_input)
  
  # Run if user inputs 0
  if desired_number_of_rounds == 0:
    clear()
    print('Take care!')
    # exit()  # Uncomment to work within Terminal
  
  # Run if user input is greater than 5
  elif desired_number_of_rounds > 5:
    print("Try a smaller number, preferably between 1 and 5")
    return ask_for_rounds()
  
  # Run if user inputs a number greater than 1
  elif desired_number_of_rounds > 1:
    print(f"Fantastic! We'll do {desired_number_of_rounds} rounds of box breathing.")
    
  # Run if user inputs 1
  else:
    print(f"Excellent! We'll do {desired_number_of_rounds} round of box breathing.")
  
  # Return the user input
  return desired_number_of_rounds


# Ask for Rounds function
def ask_for_rounds():
  """This function asks the user to input their desired number of rounds, and returns the input"""

  # Ask user to input their desired number of rounds
  print('How many rounds of breathing would you like to do?')
  user_input = input(
      'Enter a number between 1 and 5, or type "0" to exit the program: ')

  # Run if user_input contains only numbers
  if user_input.isnumeric():
    num_of_rounds = process_user_input(user_input)
    # Return the user input
    return num_of_rounds

  else:
    # Checks if user_input is a negative number or not a number
    while not user_input.isnumeric():
      if user_input == 'zero':
        num_of_rounds = process_user_input(0)
        # Return the user input
        return num_of_rounds
      elif user_input == 'one':
        num_of_rounds = process_user_input(1)
        # Return the user input
        return num_of_rounds
      elif user_input == 'two':
        num_of_rounds = process_user_input(2)
        # Return the user input
        return num_of_rounds
      elif user_input == 'three':
        num_of_rounds = process_user_input(3)
        # Return the user input
        return num_of_rounds
      elif user_input == 'four': 
        num_of_rounds = process_user_input(4)
        # Return the user input
        return num_of_rounds
      elif user_input == 'five':
        num_of_rounds = process_user_input(5)
        # Return the user input
        return num_of_rounds
      else:  
        print("Invalid input")
        return ask_for_rounds()