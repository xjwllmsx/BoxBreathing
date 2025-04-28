# Import name and system from os
from os import name, system

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
