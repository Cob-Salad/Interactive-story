from fractions import Fraction
from interface import Interface
import desolate_decisions


class Desolate(Interface):
  
    def lonely(self):
        choices  = ["Do you want to make camp for the night?", "Continue walking to the charging port?"]
        print()
        choice = self.display_options(choices)
        if choice == "1":
            self.make_camp()
        elif choice  == "2":
            self.keep_walking()
        else:
            self.wrong_choice()
    
    
    def make_camp(self):
        print(desolate_decisions.decisions["decision3"])
        print()
        choices = ["Do you make a fire for the night?", "Do you enjoy seeing how bright all the stars are?"]
        choice = self.display_options(choices)
        if choice  == "1":
            print(desolate_decisions.decisions["decision4"])
            self.injury()
        elif choice  == "2":
            print(desolate_decisions.decisions["decision5"])
            self.survival()
        elif choice == "3":
            self.display_options()
        else:
            self.wrong_choice()


    def keep_walking(self):
        self.remote_battery -= 2
        print(desolate_decisions.decisions["decision6"])
        self.survival()


    def wrong_choice(self):
        self.remote_battery -= 3
        print(f"""You have made the wrong choice and ended up in a precarious situation. 
Your remote is down to {Fraction(self.remote_battery/8)}.
                """)
        self.survival()
        

    def injury(self):
        print("You have seriously injured your arm in the fire. ")


    def survival(self):
        print(f"""
Your water level is at {self.water}.
Do you have a tool? {self.inventory}. 
Your remote battery is at {Fraction(self.remote_battery/8)}.
                """)
        choices = ["Do you go out looking for supplies? ", "Do you continue on your journey of following the map to find a charging port? "]
        print()
        choice = self.display_options(choices)
        if choice == "1":
            self.make_camp()
        elif choice  == "2":
            self.keep_walking()
        else:
            self.wrong_choice()


def main():
        
        desolate = Desolate()
        print()
        print(desolate_decisions.decisions["decision1"])
        print()
        print(desolate_decisions.decisions["decision2"])
        desolate.lonely()


      


if __name__ == "__main__":
    main()
