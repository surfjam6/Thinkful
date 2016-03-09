# pirate_bartender.py

import random

def drink_preferences(questions):
  preferences = {}
  """Asks customer preferences and created preferences dictionary"""
  for taste in questions:
    print(questions[taste])

    while True:
      answer = str.lower(input("Please enter your response: (y/n)"))
      if answer in "YyNn":
        break
      else:
        print("""Incorrect entry, please enter "y" or "n".""")
    if answer == "y":
      preferences.update({taste: True})
  return preferences
      
def construct_drink(preferences, ingredients):
  """Constructs an returns a drink"""
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

def main():
  preferences = drink_preferences(questions)
  drink = construct_drink(preferences, ingredients)
  if drink == []
    print("Your drink has no ingredients!! Please start again"
    exit()
  else:
    print("\nI have created a drink according to your preferences. It will contain:")
    for ingredient in drink:
      print("A {}".format(ingredient))
    print("""Your drink is called a "{}, {}"!!""".format(random.choice(adjective_list), random.choice(nouns_list)))
  
if __name__ == "__main__":
  main()
