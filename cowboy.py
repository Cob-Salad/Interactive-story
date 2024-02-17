from fractions import Fraction
from interface import Interface
import cowboy_decisions


class Cowboy(Interface):


    def story(self):
        choices = ["Do you steal his clothes to blend in with everyone else? ", "Do you jump out from behind the counter and yell DON\'T SHOOT!!!"]
        print()
        choice = self.display_options(choices)
        if choice == "1":
            pass
        elif choice  == "2":
            pass
        else:
            self.wrong_choice()


    def wrong_choice(self):
        self.remote_battery -= 3
        print(f"""You have made the wrong choice and ended up in a precarious situation. 
Your remote is down to {Fraction(self.remote_battery/8)}.
                """)


def main():
    cowboy = Cowboy()
    print(cowboy_decisions.decisions["decision1"])
    cowboy.story()

if __name__ == "__main__":
    main()