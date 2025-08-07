import csv

# This class represents a single item in the inventory
class InventoryItem:
    def __init__(self, name, price, quantity, restock_amount, restock_threshold):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.restock_amount = restock_amount
        self.restock_threshold = restock_threshold

    def __str__(self):
        return f"{self.name} | Qty: {self.quantity} | Threshold: {self.restock_threshold}"

    def sell(self, amount):
        if amount <= self.quantity:
            self.quantity -= amount
            print(f"Sold {amount} of {self.name}")
        else:
            print(f"Only {self.quantity} of {self.name} in stock.")

        # Check if we need to restock
        if self.quantity < self.restock_threshold:
            print(f"{self.name} is running low. Restocking...")
            self.quantity += self.restock_amount
            print(f"{self.name} restocked. New quantity: {self.quantity}")


# This class manages the whole inventory
class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print("Item added.")

    def sell_item(self, item_name, qty):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                item.sell(qty)
                return
        print("That item isn't in stock.")

    def export_to_txt(self, file_name="inventory.txt"):
        with open(file_name, "w") as file:
            for item in self.items:
                file.write(str(item) + "\n")
        print("Saved inventory to text file.")

    def export_to_csv(self, file_name="inventory.csv"):
        with open(file_name, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["name", "price", "quantity", "restock_amount", "restock_threshold"])
            for item in self.items:
                writer.writerow([item.name, item.price, item.quantity, item.restock_amount, item.restock_threshold])
        print("Saved inventory to CSV.")

    def generate_low_stock_report(self):
        found_low = False
        for item in self.items:
            if item.quantity <= item.restock_threshold:
                if not found_low:
                    print("\nLow Stock Items:")
                    found_low = True
                print(f"{item.name} | Qty: {item.quantity} | Threshold: {item.restock_threshold}")
        if not found_low:
            print("All items are stocked well.")

    def get_item_by_name(self, name):
        for item in self.items:
            if item.name.lower() == name.lower():
                return item
        return None

    def show_inventory(self):
        if not self.items:
            print("Inventory is empty.")
        else:
            print("\nInventory List:")
            for item in self.items:
                print(f"{item.name} | Price: {item.price} | Qty: {item.quantity}")


# Reads items from a CSV file and returns them as InventoryItem objects
def load_from_csv(file_name="inventory.csv"):
    items = []
    try:
        with open(file_name, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row["name"]
                price = int(row["price"])
                quantity = int(row["quantity"])
                restock_amount = int(row["restock_amount"])
                restock_threshold = int(row["restock_threshold"])
                items.append(InventoryItem(name, price, quantity, restock_amount, restock_threshold))
    except FileNotFoundError:
        print("CSV file not found.")
    return items


# Simple CLI app for the user to interact with inventory
def main():
    store = Inventory()

    while True:
        print("\n======= Inventory Menu =======")
        print("1. Add Item")
        print("2. Sell Item")
        print("3. Show Inventory")
        print("4. Save as Text File")
        print("5. Save as CSV")
        print("6. Load from CSV")
        print("7. Check Low Stock")
        print("8. Exit")

        choice = input("Choose an option (1-8): ")

        if choice == "1":
            name = input("Item name: ")
            price = int(input("Price: "))
            quantity = int(input("Quantity: "))
            restock_amount = int(input("Restock amount: "))
            restock_threshold = int(input("Restock threshold: "))
            item = InventoryItem(name, price, quantity, restock_amount, restock_threshold)
            store.add_item(item)

        elif choice == "2":
            name = input("Item to sell: ")
            qty = int(input("How many? "))
            store.sell_item(name, qty)

        elif choice == "3":
            store.show_inventory()

        elif choice == "4":
            store.export_to_txt()

        elif choice == "5":
            store.export_to_csv()

        elif choice == "6":
            items = load_from_csv()
            for item in items:
                store.add_item(item)

        elif choice == "7":
            store.generate_low_stock_report()

        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("Pick a valid number (1-8).")

if __name__ == "__main__":
    main()                           
                               
                            
                            
                            
                            
                            
                              
                          
                              
                              
                              
                              
                  
                              
                              
                              
                              
                             
                             
                      
                      
                      
                      