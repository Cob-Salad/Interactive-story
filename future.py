from interface import Interface

#vent_key = [1, 2, 2, 1, 3]
#vent_list = []
#at_vault = False
class Vault(Interface):

    def __init__(self) -> None:
        self.vent_key = [1, 2, 2, 1, 3]
        self.vent_list = []
        self.at_vault = False 

    def turn_left(self):
        self.vent_list.append(1)
        print("You make a left turn.")

    def turn_right(self):
        self.vent_list.append(2)
        print("You make a right turn.")

    def go_straight(self):
        self.vent_list.append(3)
        print("You continue straight.")

    def break_down(self):
        if self.vent_list == self.vent_key:
            print("You made it to the vault door!")
            self.at_vault = True
            self.future_vault()
        else:
            print("Wrong Hallway! You Have Been Spotted!")
            
    def navigate_vents(self):
        print("You have finally made it! After sneaking into one of the premiere \
secure facilities in this solar system, you find yourself within a maze of vents.")
        print("You must follow the instructions you bought with the last of your money EXACTLY.")
        while not self.at_vault:
            direction = 0
            direction = int(input("Which Direction? "))
            if direction == 1:
                self.turn_left()
            elif direction == 2:
                self.turn_right()
            elif direction == 3:
                self.go_straight()
            elif direction == 4:
                self.break_down()
            else:
                break
        
    def future_vault(self):
        print("You see the vault door before you. You feel the slight shake of excitement as you pull out your interface in order to pull out the passkey")



vault = Vault()


vault.navigate_vents()

    

