from future import Vault
from desolate import desolate

class Interface():

    def __innit__(self, ):
        pass


    def choice(self, choice1: str):
        list_choices = []
        list_choices.insert(0, "1. Interface")
        option_picked = int(input("Input your choice: "))
        option_picked -= 1

        if option_picked == 0:
            print("WELCOME TO YOUR INTERFACE")
        elif option_picked == 1:
            print(choice1)
        elif option_picked == 2:
            pass
        elif option_picked == 3:
            pass
        elif option_picked == 4:
            pass

    def battery_level():
        pass

    def inventory():
        pass

    def map():
        print("You project a holographic \
    map of the vent sytem of the \
    compound surrounding the vault")
        print("From the beginning \
    of the maze of vents you need to go \
    Left, Right, Right, Left, Straight")
        
    
   
Vault.turn_left()

map()
    
desolate()