# pirate_bartender.py

import random

def get_customer_name():
  """Asks customer for name"""  
  name = str.capitalize(input("Please enter your name: "))
  return name
  
def customer_lookup(name, customer_preferences_list):
  if name in customer_preferences_list:
    use_previous = str.lower(input("Would you like to use your previous preferences ? {}\n".format(customer_preferences_list[name])))
    if use_previous in "y":
      return True

def drink_preferences(questions):
  preferences = []
  """Asks customer preferences and created preferences dictionary"""
  for taste in questions:
    print(questions[taste])

    while True:
      answer = str.lower(input("Please enter your response: (y/n)"))
      if answer in "yn":
        break
      else:
        print("""Incorrect entry, please enter "y" or "n".""")
    if answer == "y":
      preferences.append(taste)
  return preferences
      
def construct_drink(preferences, ingredients):
  """Constructs and returns a drink"""
  drink = []
  for taste in preferences:
    drink.append(random.choice(ingredients[taste]))
  return drink


questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

adjective_list = ["Sporty","Fast", "Noisy", "Fluffy", "Squishy", "Green", "Blue", "Icy", "Chilled", "Spotted", "Snowy"]
nouns_list = ["Owl", "Dog", "Lizard", "Hurricane", "Twister", "Slurpy", "Hawk", "Mouse"]
customer_preferences_list = {}

def main():
  
  while True:
    name = get_customer_name()
    found = customer_lookup(name, customer_preferences_list)
    if found:
      preferences = customer_preferences_list[name]
    else:
      preferences = drink_preferences(questions)
    customer_preferences_list.update({name: preferences})
#    print(customer_preferences_list)
    drink = construct_drink(preferences, ingredients)
    if not drink:
      print("Your drink has no ingredients!! Please try again")
    else:
      print("\nI have created a drink according to your preferences. It will contain:")
      for ingredient in drink:
        print("A {}".format(ingredient))
      print("""Your drink is called a "{}, {}"!!""".format(random.choice(adjective_list), random.choice(nouns_list)))
    print("")
    print("Would you like another drink?")
    # Loop to check for legal entry:
    while True:
      repeat = str.lower(input("Please enter your response: (y/n)"))
      print(repeat)
      if repeat in "yn":
        break
      else:
        print("""Incorrect entry, please enter "y" or "n".""")
    if repeat not in "y":
      print("Goodbye")
      break
  
if __name__ == "__main__":
  main()
