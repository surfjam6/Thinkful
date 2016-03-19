# pirate_barsupply_countder.py
import random
import bar
import bar_data

def main():
  
  while True:
    name = bar.get_customer_name()
    found = bar.customer_lookup(name, bar_data.customer_preferences_list)
    if found:
      preferences = bar_data.customer_preferences_list[name]
    else:
      preferences = bar.drink_preferences(bar_data.questions)
    bar_data.customer_preferences_list.update({name: preferences})
#    print(customer_preferences_list)
    drink = bar.construct_drink(preferences, bar_data.ingredients)
    if not drink:
      print("Your drink has no ingredients!! Please try again")
    else:
      print("\nI have created a drink according to your preferences. It will contain:")
      for ingredient in drink:
        print("A {}".format(ingredient))
        bar.bar(ingredient, bar_data.inventory)
      print("""Your drink is called a "{}, {}"!!""".format(random.choice(bar_data.adjective_list), random.choice(bar_data.nouns_list)))
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
