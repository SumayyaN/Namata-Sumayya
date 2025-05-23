#Activity one

inventory = {}

while True:
    print("\nInventory Management System")
    print("1. Add Item to Inventory")
    print("2. Remove Item from Inventory")
    print("3. Update Item Quantity")
    print("4. View Current Inventory")
    print("5. Exit")
    
    choice = input("Enter an option (1-5): ")
 
    #ADD ITEM
    if choice == '1': 
        item = input("Enter item name: ").strip()
        if item in inventory:
            print(f"Error: {item} already exists in inventory!")
            continue
        try:
            quantity = int(input("Enter initial quantity: "))
            if quantity < 0:
                print("Warning: Quantity cannot be negative! Setting to 0.")
                quantity = 0
            inventory[item] = quantity
            print(f"{item} added with quantity {quantity}")
        except ValueError:
            print("Invalid input! Please enter a valid number for quantity.")
            
    # Remove Item
    elif choice == '2':  
        item = input("Enter item name to remove: ").strip()
        if item in inventory:
            del inventory[item]
            print(f"{item} removed from inventory")
        else:
            print(f"Error: {item} not found in inventory!")
            
    # Modify Quantity
    elif choice == '3':  
        item = input("Enter item name to modify: ").strip()
        if item in inventory:
            try:
                change_quantity = int(input("Enter quantity to add (use negative number to reduce): "))
                new_quantity = inventory[item] + change_quantity
                if new_quantity < 0:
                    print("Warning: Stock cannot be negative! Setting quantity to 0.")
                    new_quantity = 0
                inventory[item] = new_quantity
                print(f"{item} quantity modified. New quantity: {new_quantity}")
            except ValueError:
                print("Invalid input! Quantity not modified.")
        else:
            print(f"Error: {item} not found in inventory!")

    # View Inventory
    elif choice == '4':  
        if not inventory:
            print("Inventory is empty!")
        else:
            print("\nCurrent Inventory:")
            print("-" * 20)
            for item, quantity in inventory.items():
                print(f"{item.ljust(15)} | {str(quantity).rjust(3)}")
            print("-" * 20)

    elif choice == '5':  # Exit Program
        print("Exiting inventory management system. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 5.")
