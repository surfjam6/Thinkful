# side_effect_test.py
def print_function():
   """I'm also a function, but I don't take any parameters"""
   print("I'm {}, and I'm printing now".format(print_function.__name__))
   
def side_effect_test(value):
  # Do something to modify the value
#  value[1] = "orange"
#  value = 10
#  value['dog'] = 'wag'
#  value = "Jamie Weisbrod"
#  value = True
  value = (4,5,6)
  print("Inside the function, the value becomes {}".format(value))
  return value 
  
if __name__ == '__main__':
  print_function()
  # Create the value
#  value = ["red", "green", "blue"]
#  value = 0
#  value = {"cat": "meow", "dog": "bark", "mouse": "squeak"}
#  value = "Jamie"
##  value = bool(0) # False
##  value - bool("0") # True
  value = (1, 2, 3)
  print("Outside the function, the value starts as {}".format(value))
  returned_value = side_effect_test(value)  
  print("Outside the function, the value is now {}".format(value))  
  print("Returned value is now {}".format(returned_value))  

