# biycle_main/py

import bicycles
import bike_inventory

customer_list = []
def main():
    while True:
        JoesBicycleStore = bicycles.Bike_Shop("""Joe's Bicycle Store""", bike_inventory.bicycle_inventory, .20)
        Customer_1 = bicycles.Customer("John Smith", 200.00, "yes")
        customer_list.append(Customer_1) 
        Customer_2 = bicycles.Customer("Jane Appleton", 500.00, "yes")
        customer_list.append(Customer_2) 
        Customer_3 = bicycles.Customer("Byron Greene", 1000.00, "yes")
        customer_list.append(Customer_3) 
        print(JoesBicycleStore.name)
        print(JoesBicycleStore.inventory)
        print(JoesBicycleStore.inventory["mountain_bike"])
        print(JoesBicycleStore.margin)
        for i in range(len(customer_list)):
            print("Customer Name: {}, Budget: ${:,.2f}".format(customer_list[i].name, customer_list[i].budget))
        break
        


if __name__ == "__main__":
  main()
