from abc import ABC, abstractmethod
class Cowboy:

    def __init__(self, water: str, knife: bool):
        self.water = water
        self.knife = knife
    
    @abstractmethod
    def inventory(self):
        self.remote_battery = 2

    def story(self):
       decision1 = input('''Do you steal his clothes to blend in with everyone else?(1)
                         or
Do you jump out from behind the counter and yell "DON'T SHOOT!!!(2)"''')
       if decision1 == "1":
           pass
       elif decision1 == "2":
           pass
       else:
           pass


def main():
    cowboy = Cowboy()
    print("""You quickly find yourself in another world. You hear shots being fired left and right.
You hear bullets whizzing by your head. You duck behind the counter, hoping no one noticed you popping up out of no where.
You see a man passed out behind the counter presumably from drinking. 
       """)
    cowboy.story()

if __name__ == "__main__":
    main()