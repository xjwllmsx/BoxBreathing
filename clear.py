from os import name, system


def clear():
    # checks for windows os, else runs clear function of mac and linux
    _ = system("cls") if name == "nt" else system("clear")
