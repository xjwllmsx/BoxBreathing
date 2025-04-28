# from os import name, system # Uncomment for use in terminal
from IPython.display import clear_output  # Used for clearing Juypter Notebook cell


def clear():
    # _ = system("cls") if name == "nt" else system("clear")  # checks for windows os, else runs clear function of mac and linux
    clear_output(wait=True)  # clears Juypter notebook cell
