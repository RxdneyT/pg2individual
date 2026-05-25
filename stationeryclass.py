# This class represents a stationery item and stores its details (name, quantity and cost)
class Stationery:
    # Constructor to initialise the attributes of each stationery item
    # Parameters: name (string), quantity (int), cost (float)
    def __init__(self, name, quantity, cost):
        self.name = name
        self.quantity = quantity
        self.cost = cost

   # Method to calculate and return the total cost of the stationery item (in Stationery class)
    def calculate_total_cost(self):        
        return self.quantity * self.cost