from interface import Interface
import sys
import time

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
            sys.exit(0)
            
    def navigate_vents(self):
        print("You have finally made it! After sneaking into one of the premiere \
secure facilities in this solar system, you find yourself within a maze of vents.")
        print("You must follow the map you bought EXACTLY.")
        Interface.map()
        print("Current options: ")
        print("1. Left Turn, 2. Right Turn, 3. Go Straight, 4. Leave Vents, 5. Back to Start")
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
            elif direction == 5:
                self.vent_list.clear()
                print("You successfully made it back to the start")
                print("Current options: ")
                print("1. Left Turn, 2. Right Turn, 3. Go Straight, 4. Leave Vents, 5. Back to Start")
            else:
                break
        
    def future_vault(self):
        print("You see the vault door before you. You feel the slight\
 shake of excitement as you behold the surprisingly old and simple keyhole.")
        open_vault = input(print("Use the lockpicking function of your interface? (y/n): "))
        if open_vault == "y":
            self.enter_vault()
        else:
            sure = input(print("Are you sure you want to turn back now? (y/n) "))
            if sure == "y":
                print("Oh no! The periodic security scan hit you! You better get running!")
            else:
                self.future_vault()

    def enter_vault(self):
        print("You hold out your hand to the keyhole as a multitude \
of small robotic arms shoot out and almost instantly you hear the click of success.")
        print()
        print("The large vault door slowly swings open to reveal a \
pedestal with a seemingly ordinary, if vintage, remote.")
        remote = " "
        remote = str(input(print("Proceed and pickup the remote? (y/n): ")))
        if remote == "y":
            print(".")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print(".")
            print("As you step towards your bounty you suddenly feel a \
light pulse of energy across your skin and suddenly the bright welcoming \
lights turn to a menacing red.")
            time.sleep(1)
            print("Oh no! The periodic security scan hit you! You better get moving!")
            print("BEEP")
            time.sleep(1)
            print("BEEP")
            time.sleep(1)
            print("BEEP")
            time.sleep(1)
            print("BEEP")
            time.sleep(1)
            print()
            print("You remember that this remote supposedly has some sort \
of teleportation function, maybe it can get you out of here?")
            print("There are so many buttons on the remote!")
            button = ""
            button = input(print("Which one do you press? (blue/yellow/green/red)"))
            if button == "blue" or button == "yellow" or button == "green" or button == "red":
                print("The remote begins humming louder and louder.")
                time.sleep(3)
                print("Maybe this wasn't such a good idea...")
            else:
                print("The remote begins humming louder and louder.")
                time.sleep(3)
                print("Maybe this wasn't such a good idea...") 
                
        else:
            print("Oh no! The periodic security scan hit you! You better get moving!")


       





vault = Vault()

vault.enter_vault()
#vault.navigate_vents()

    

