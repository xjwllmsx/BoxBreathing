# Import delay function from breathInAndOut
from .breathInAndOut import delay

# Import clear() from utils
from .utils import clear


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
