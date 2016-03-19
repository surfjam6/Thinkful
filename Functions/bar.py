import random
import bar_data

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

def bar(ingredient, inventory):
    inventory[ingredient] -= 1
    if inventory[ingredient] < bar_data.supply_count/2:
        restock = str.lower(input("Inventory of {} is low, should I restock?(y/n)\n".format(inventory[ingredient])))
        if restock not in "n":
            bar_data.inventory[ingredient] = bar_data.supply_count
            print("I am restocking {}".format(inventory[ingredient]))
