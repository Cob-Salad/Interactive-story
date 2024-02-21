import sys
from colorama import Fore, Style, init
from interface import Interface
import cowboy_decisions

class Cowboy(Interface):

    init(autoreset=True)
    KEY = 3579

    def story(self):
        print()
        Interface.print_slow_color("Wild West", "33")
        print()
        print()
        Interface.print_slow(cowboy_decisions.decisions["decision1"])
        choices = ["Blend in with everyone else? ", "Jump out from behind the counter?"]
        print()
        choice = self.display_options(choices)
        if choice == "1":
            Interface.print_slow(cowboy_decisions.decisions["decision2"])
            self.add_to_inventory("random person's clothes")
            self.blend_in()
        elif choice  == "2":
            Interface.print_slow(cowboy_decisions.decisions["decision3"])
            self.remote_battery -= 1
            self.do_not_shoot()
        else:
            self.stored_state.append(self.story)
            self.wrong_choice()


    def blend_in(self):
        print()
        Interface.print_slow(cowboy_decisions.decisions["decision4"])
        choices = ["Stop and get them a drink?", "Keep walking out?"]
        print()
        choice = self.display_options(choices)
        if choice == "1":
            Interface.print_slow(cowboy_decisions.decisions["decision5"]) 
            self.become_the_bartender()
        elif choice  == "2":
            Interface.print_slow(cowboy_decisions.decisions["decision6"])
            self.the_end()
        else:
            self.stored_state.append(self.blend_in)
            self.wrong_choice()

    def become_the_bartender(self):
        print()
        Interface.print_slow(cowboy_decisions.decisions["decision7"])
        choices = ["Befriend the Saloon patrons?", "Continue to sneak away?"]
        print()
        choice = self.display_options(choices)
        if choice == "1":
            Interface.print_slow(cowboy_decisions.decisions["decision8"])
            self.add_to_inventory("new friends")
            self.break_in()
        elif choice  == "2":
            Interface.print_slow(cowboy_decisions.decisions["decision9"])
            self.the_end()
        else:
            self.stored_state.append(self.become_the_bartender)
            self.wrong_choice()

    def break_in(self):
        print()
        Interface.print_slow(cowboy_decisions.decisions["decision10"])
        choices = ["Convince your new friends?", "Break in alone?"]
        print()
        choice = self.display_options(choices)
        if choice == "1":
            Interface.print_slow(cowboy_decisions.decisions["decision11"])
            self.code_key()
            self.to_the_vault()
        elif choice  == "2":
            Interface.print_slow(cowboy_decisions.decisions["decision12"])
            self.the_end()
        else:
            self.stored_state.append(self.break_in)
            self.wrong_choice()

    def to_the_vault(self):
        print()
        Interface.print_slow(cowboy_decisions.decisions["decision13"])
        choices = ["Let everyone else in behind you?", "Quickly lock the window behind you?"]
        print()
        choice = self.display_options(choices)
        if choice == "1":
            Interface.print_slow(cowboy_decisions.decisions["decision14"])
            self.remote_battery -= 1 
            self.enter_code()
        elif choice  == "2":
            Interface.print_slow(cowboy_decisions.decisions["decision15"])
            self.enter_code()
        else:
            self.stored_state.append(self.break_in)
            self.wrong_choice() 

    def do_not_shoot(self):
        print()
        Interface.print_slow(cowboy_decisions.decisions["decision16"])
        choices = ["Will you survive to tell the tale?", "Will this be the end?"]
        print()
        choice = self.display_options(choices)
        if choice == "1":
            Interface.print_slow(cowboy_decisions.decisions["decision17"])
            self.the_end()
        elif choice  == "2":
            Interface.print_slow(cowboy_decisions.decisions["decision18"])
            self.fully_charged()
        else:
            self.stored_state.append(self.do_not_shoot)
            self.wrong_choice() 

    def code_key(self):
        if self.remote_battery >= 1:
            Interface.print_color(f"""This is the combination {self.KEY}.
Remember this combination it as this is the only time you will see it.""", "32")
            print()
        else:
            self.remote_battery == 0
            Interface.print_color("You do not have enough battery in your remote to view the combination. You will have to guess and hope you get it right.", "31")
            print()

    def enter_code(self):
        tries = 3
        print()
        Interface.print_slow("It is time to enter your combination. ")
        for i in range(3):
            Interface.print_slow(f"You have {tries} tries. ")
            print()
            if tries == 0:
                print()
                Interface.print_slow("You have not guessed the combination to get into the vault.")
                self.the_end()
            code = int(input("Enter the combination: "))
            tries -= 1
            if code == self.KEY:
                Interface.print_slow("You did it!")
                print()
                self.fully_charged()
                break

    def fully_charged(self):
        print()
        Interface.print_color("""You have made it to the charging port. 
You plug-in the remote to start charging. The remote charges quickly.
You have learned how to operate the remote and are trying to decide where to go to next.
You are unsure of what you would like to do. Maybe you will continue to travel and time hop?
Maybe you will go back to your original world and try to pretend like nothing has happened.
Either way you knnw nothing will be the same.......        
              
________________________________THE_END________________________________________""","36")
        print()
       


    def the_end(self):
        Interface.print_color("You don't make it to the charging port. You never make it out of this world." , "31")
        sys.exit(0)

cowboy = Cowboy()
cowboy.story()



