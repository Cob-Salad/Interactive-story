class Interface():

    def __innit__(self, ):
        pass


    def choice(self, choice1: str, choice2: str, choice3: str, choice4: str, choice5: str):
        list_choices = []
        list_choices.insert(0, "1. Interface")
        list_choices.append(choice1)
        list_choices.append(choice2)
        list_choices.append(choice3)
        list_choices.append(choice4)
        list_choices.append(choice5)
        option_picked = int(input("Input your choice: "))
        option_picked -= 1


        if option_picked == 0:
            print("WELCOME TO YOUR INTERFACE")
        elif option_picked == 1:
            list_choices.append(choice1)
        elif option_picked == 2:
            list_choices.append(choice2)
        elif option_picked == 3:
            list_choices.append(choice3)
        elif option_picked == 4:
            list_choices.append(choice4)
        elif option_picked == 5:
            list_choices.append(choice5)


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