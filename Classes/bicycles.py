# bicycles.py

class Bicycle(object):
    def __init__(self, model, weight, cost):
        self.model = model
        self.weight = weight
        self.cost = cost

class Bike_Shop(object):
    def __init__(self, name, inventory, margin):
        self.name = name
        self.inventory = inventory
        self.margin = margin

class Customer(object):
    def __init__(self, name, budget, ready_to_buy):
        self.name = name
        self.budget = budget
        self.ready_to_buy = ready_to_buy

