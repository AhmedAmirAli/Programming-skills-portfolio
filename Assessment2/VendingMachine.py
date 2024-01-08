import json

class VendingMachine:
    def __init__(self, machine_type):
        self.machine_type = machine_type
        self.load_inventory()

    def load_inventory(self):
        try:
            with open(f"{self.machine_type}_inventory.json", "r") as file:
                self.inventory = json.load(file)
        except FileNotFoundError:
            print(f"Error: Inventory file for {self.machine_type} not found.")
            exit()

    def save_inventory(self):
        with open(f"{self.machine_type}_inventory.json", "w") as file:
            json.dump(self.inventory, file)

    def display_menu(self):
        print(f"\nAvailable Items in {self.machine_type} Vending Machine:")
        for item, details in self.inventory.items():
            print(f"{item} - ${details['price']} ({details['quantity']} available)")

    def make_purchase(self):
        self.display_menu()
        item = input("Enter the item you want to purchase: ")

        if item in self.inventory:
            quantity_available = self.inventory[item]['quantity']
            if quantity_available > 0:
                price = self.inventory[item]['price']
                print(f"Price: ${price}")
                quantity = int(input("Enter the quantity: "))

                total_cost = price * quantity

                print(f"Total Cost: ${total_cost}")

                confirmation = input("Confirm purchase? (yes/no): ").lower()
                if confirmation == 'yes':
                    self.inventory[item]['quantity'] -= quantity
                    self.save_inventory()

                    print(f"Purchase successful! Total cost: ${total_cost}")
                else:
                    print("Purchase canceled.")
            else:
                print("Sorry, the selected item is out of stock.")
        else:
            print("Invalid item. Please select a valid item.")

class User:
    def __init__(self, valid_machine_types):
        self.valid_machine_types = valid_machine_types

    def switch_machine(self, new_machine_type):
        if new_machine_type in self.valid_machine_types:
            return VendingMachine(new_machine_type)
        else:
            print("Invalid vending machine type. Please choose from the available types.")
            return None

def main():
    valid_machine_types = ['drinks', 'snacks', 'bento']
    user = User(valid_machine_types)

    machine_type = input(f"Enter the type of vending machine ({', '.join(valid_machine_types)}): ").lower()

    while machine_type not in valid_machine_types:
        print("Invalid vending machine type. Please choose from the available types.")
        machine_type = input(f"Enter the type of vending machine ({', '.join(valid_machine_types)}): ").lower()

    vending_machine = user.switch_machine(machine_type)

    while vending_machine:
        print("\nSelect an action:")
        print("1. View Menu")
        print("2. Make a Purchase")
        print("3. Switch Vending Machine Type")
        print("4. Exit")

        action = input("Enter the number of your choice: ")

        if action == '1':
            vending_machine.display_menu()
        elif action == '2':
            vending_machine.make_purchase()
        elif action == '3':
            new_machine_type = input(f"Enter the new vending machine type ({', '.join(valid_machine_types)}): ").lower()
            vending_machine = user.switch_machine(new_machine_type)
        elif action == '4':
            print("Thank you for using the Vending Machine!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()