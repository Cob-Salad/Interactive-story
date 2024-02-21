from interface import Interface
from future import Vault
from desolate import Desolate
from cowboy import Cowboy
#from wizard import


class Main(Interface):

    def __init__(self):
        self.vault = Vault()
        self.desolate = Desolate()
        self.cowboy = Cowboy()
        #Add wizard
               
    def run(self):
        self.vault.navigate_vents()      
        self.desolate.arrived()
        self.cowboy.story()
        #Add Wizard.py
       

if __name__ == "__main__":
    main = Main()
    main.run()
