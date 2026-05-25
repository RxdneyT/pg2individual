import csv
# Import the Stationery class from stationeryclass.py to calculate total cost
from stationeryclass import Stationery

# Initial inventory data stored as a list of dictionaries
# Each dictionary represents one stationery item with its details
inventory = [
    {"name": "Pen", "quantity": 200, "cost": 1.20, "total_cost": 240.0},
    {"name": "Pencil", "quantity": 250, "cost": 0.80, "total_cost": 200.0},
    {"name": "Eraser", "quantity": 150, "cost": 0.50, "total_cost": 50.0},
    {"name": "Glue_stick", "quantity": 100, "cost": 1.10, "total_cost": 110.0},
    {"name": "Writing_Book", "quantity": 300, "cost": 1.50, "total_cost": 450.0}
]

def main():
    # Main loop - keeps the program running until user chooses to exit
    while True:
        # Display the menu options
        print()
        print("====================================================")
        print("  STATIONERY INVENTORY MANAGEMENT SYSTEM")
        print("====================================================")
        print("1 - To enter new stationery item")
        print("2 - To edit the stationery item")
        print("3 - To update the stationery item which was sold")
        print("4 - To display all the stationery items")
        print("5 - To save the list of all the stationery items in .CSV file")
        print("====================================================")

        # Get the user's menu choice and remove any extra whitespace
        option = input("Enter your choice (1-5): ").strip()

        if option == "1":
            # Option 1 - Add a new stationery item to the inventory
            name = input("Enter the name of the stationery item: ")

            # Loop until a valid whole number is entered for quantity
            while True:
                try:
                    quantity = int(input("Enter the quantity: "))
                    break
                except ValueError:
                    print("Invalid input! Please enter a whole number.")

            # Loop until a valid decimal number is entered for cost
            while True:
                try:
                    cost = float(input("Enter the cost: "))
                    break
                except ValueError:
                    print("Invalid input! Please enter a valid price.")

            # Create a Stationery object to calculate the total cost using the class method
            item = Stationery(name, quantity, cost)
            total_cost = item.calculate_total_cost()

            # Append the new item as a dictionary into the inventory list
            inventory.append({"name": name, "quantity": quantity, "cost": cost, "total_cost": total_cost})
            print(f"{name} has been added successfully!")

        elif option == "2":
            # Option 2 - Edit an existing stationery item
            search_name = input("Enter the name of the item to edit: ")

            # Loop through inventory to find the item by name (case-insensitive)
            for item in inventory:
                if item["name"].lower() == search_name.lower():
                    # Display current details before editing
                    print(f"Current details: Name: {item['name']}, Quantity: {item['quantity']}, Cost: {item['cost']}")
                    new_name = input("Enter the new name: ")

                    # Loop until a valid whole number is entered for new quantity
                    while True:
                        try:
                            new_quantity = int(input("Enter the new quantity: "))
                            break
                        except ValueError:
                            print("Invalid input! Please enter a whole number.")

                    # Loop until a valid decimal number is entered for new cost
                    while True:
                        try:
                            new_cost = float(input("Enter the new cost: "))
                            break
                        except ValueError:
                            print("Invalid input! Please enter a valid price.")

                    # Update the item's details in the inventory
                    item["name"] = new_name
                    item["quantity"] = new_quantity
                    item["cost"] = new_cost
                    item["total_cost"] = new_quantity * new_cost
                    print(f"{search_name} has been updated successfully!")
                    break

            # The else block runs only if the for loop completed without finding the item
            else:
                print("Item not found!")

        elif option == "3":
            # Option 3 - Update stock quantity after a sale
            search_name = input("Enter the name of the item sold: ")

            # Loop until a valid whole number is entered for quantity sold
            while True:
                try:
                    quantity_sold = int(input("Enter the quantity sold: "))
                    break
                except ValueError:
                    print("Invalid input! Please enter a whole number.")

            # Loop through inventory to find the item by name (case-insensitive)
            for item in inventory:
                if item["name"].lower() == search_name.lower():

                    # Validate that quantity sold does not exceed current stock
                    while quantity_sold > item["quantity"]:
                        print(f"Invalid! Quantity sold cannot exceed current stock ({item['quantity']}).")
                        while True:
                            try:
                                quantity_sold = int(input("Enter the quantity sold: "))
                                break
                            except ValueError:
                                print("Invalid input! Please enter a whole number.")

                    # Deduct quantity sold and recalculate total cost
                    item["quantity"] = item["quantity"] - quantity_sold
                    item["total_cost"] = item["quantity"] * item["cost"]
                    print(f"{search_name} has been updated successfully!")
                    break

            # The else block runs only if the for loop completed without finding the item
            else:
                print("Item not found!")

        elif option == "4":
            # Option 4 - Display all stationery items in a formatted table
            print("\n" + "="*60)
            # Print table headers with fixed column widths for alignment
            print(f"{'No.':<5}{'Name':<20}{'Quantity':<12}{'Cost':>8}{'Total Cost':>12}")
            print("="*60)
            # Loop through inventory and print each item with its index number
            for index, item in enumerate(inventory, start=1):
                print(f"{index:<5}{item['name']:<20}{item['quantity']:<12}{item['cost']:>8.2f}{item['total_cost']:>12.2f}")
            print("="*60)

        elif option == "5":
            # Option 5 - Save all inventory data to a CSV file
            # The 'with' statement automatically closes the file when done
            with open("inventory.csv", "w", newline="") as file:
                writer = csv.writer(file)
                # Write the header row
                writer.writerow(["No.", "Name", "Quantity", "Cost", "Total Cost"])
                # Write each inventory item as a row in the CSV file
                for index, item in enumerate(inventory, start=1):
                    writer.writerow([index, item["name"], item["quantity"], item["cost"], item["total_cost"]])
            print("Inventory saved to inventory.csv successfully!")

        else:
            # Handle invalid menu option input
            print("Invalid option! Please enter a number between 1 and 5.")

        # Ask user if they want to continue using the program
        continue_choice = input("\nDo you want to continue? (Y/N): ").strip().upper()

        # Keep asking until a valid Y or N is entered
        while continue_choice not in ("Y", "N"):
            print("Invalid choice. Please enter Y or N.")
            continue_choice = input("Do you want to continue? (Y/N): ").strip().upper()

        if continue_choice == "Y":
            # Clear the screen by printing blank lines and loop back to menu
            print("\n" * 50)
        elif continue_choice == "N":
            # Exit the program
            print("Thank you for using the Stationery Inventory Management System. Goodbye!")
            break

# Call the main function to start the program
main()
