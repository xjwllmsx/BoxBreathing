# Import name and system from os
from os import name, system

# Import sleep() from time module
from time import sleep

# Used for clearing Juypter Notebook cell
from IPython.display import clear_output

# Import exit() from sys module
from sys import exit


def is_running_in_notebook():
    """This function determines if the app is running in a terminal window or a Juypter notebook"""
    try:
        shell = get_ipython().__class__.__name__
        if shell == "ZMQInteractiveShell":
            return True
        elif shell == "TerminalInteractiveShell":
            return False
        else:
            return False
    except NameError:
        return False


def clear():
    """This function clears the terminal or Juypter cell window it is running in"""
    if not is_running_in_notebook():  # Runs if the app is running in a terminal window
        _ = (
            system("cls") if name == "nt" else system("clear")
        )  # checks for windows os, else runs clear function of mac and linux
    else:  # Runs if app is running in a Juypter notebook
        clear_output(wait=True)


def exit_app():
    """The function exits the app"""
    if not is_running_in_notebook():
        exit()


# Ask for Rounds function
def ask_for_rounds():
    """This function asks the user to input their desired number of rounds, and returns the input"""

    # Ask user to input their desired number of rounds
    print("How many rounds of breathing would you like to do?")
    user_input = input(
        'Enter a number between 1 and 5, or type "0" to exit the program: '
    )

    # Run if user_input contains only numbers
    if user_input.isnumeric():
        num_of_rounds = process_user_input(user_input)
        # Return the user input
        return num_of_rounds

    else:
        # Checks if user_input is a negative number or not a number
        while not user_input.isnumeric():
            if user_input == "zero":
                num_of_rounds = process_user_input(0)
                # Return the user input
                return num_of_rounds
            elif user_input == "one":
                num_of_rounds = process_user_input(1)
                # Return the user input
                return num_of_rounds
            elif user_input == "two":
                num_of_rounds = process_user_input(2)
                # Return the user input
                return num_of_rounds
            elif user_input == "three":
                num_of_rounds = process_user_input(3)
                # Return the user input
                return num_of_rounds
            elif user_input == "four":
                num_of_rounds = process_user_input(4)
                # Return the user input
                return num_of_rounds
            elif user_input == "five":
                num_of_rounds = process_user_input(5)
                # Return the user input
                return num_of_rounds
            else:
                print("Invalid input")
                return ask_for_rounds()


def process_user_input(user_input):
    """Using conditional statements, this function will generate the proper output based on the user's input"""
    # If user_input is a number, convert from string to int
    desired_number_of_rounds = int(user_input)

    # Run if user inputs 0
    if desired_number_of_rounds == 0:
        clear()
        print("Take care!")
        exit_app()

    # Run if user input is greater than 5
    elif desired_number_of_rounds > 5:
        print("Try a smaller number, preferably between 1 and 5")
        return ask_for_rounds()

    # Run if user inputs a number greater than 1
    elif desired_number_of_rounds > 1:
        print(
            f"Fantastic! We'll do {desired_number_of_rounds} rounds of box breathing."
        )

    # Run if user inputs 1
    else:
        print(f"Excellent! We'll do {desired_number_of_rounds} round of box breathing.")

    # Return the user input
    return desired_number_of_rounds


# Delay function
def delay():
    """Adds a delay of 1 second before the next out"""
    sleep(1)


# Breath In function
def round_of_breath():
    """Prints prompts for user to begin breathing in for 4 seconds"""
    cycles = ["Breath in...", "Hold...", "Breath out...", "Hold..."]
    # delay()
    for i in cycles:
        clear()
        print(i)
        delay()
        j = 4
        while j >= 1:
            print(j)
            j -= 1
            delay()


# Countdown function
def countdown():
    """Prints a countdown for the user"""
    i = 5
    clear()
    print("We'll begin in...")
    delay()
    while i >= 1:
        print(i)
        i -= 1
        delay()
    print("Let's begin!")
    delay()
