# Import sleep() from time module
from time import sleep
# Import clear() from replit module
from clear import clear

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