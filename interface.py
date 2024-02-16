from fractions import Fraction
import sys

class Interface():

    def __init__(self):
        self.inventory = []
        self.remote_battery = 4.0
        self.water = 0
  
    def add_to_inventory(self, item):
        self.inventory.append(item)
        print(f"You added {item.__class__.__name__} to your inventory. ")

    def check_inventory(self):
        print()
        print(f"""Your inventory is currently:
Inventory: {self.inventory},
Battery: {Fraction(self.remote_battery/8)},
Water: {self.water}""")
        print()
        
    def display_options(self, list_options: list):
        list_options += ["Check Inventory", "Quit"]
        while True:
            print()
            print("Options: ")
            for i in range(len(list_options)):
                print(f"{i+1}. {list_options[i]}")
            print()
            choice = input("Enter your choice: ").lower()
            if choice == str(len(list_options) - 1):
                self.check_inventory()
                continue
            elif choice ==  str(len(list_options)):
                print("Well... it is your loss. ")
                sys.exit(0)
            return choice


    def map():
        print("You project a holographic \
    map of the vent sytem of the \
    compound surrounding the vault")
        print("From the beginning \
    of the maze of vents you need to go \
    Left, Right, Right, Left, Straight")