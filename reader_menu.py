
#   13th August 2025

#   This is the reader menu. 
#   Its purpose is to provide a way for using the program. 

#   Import the single game object
from single_game import * 

class ReaderMenu:

    def __init__(self, glist):
        self.glist = glist

    #   Introduction
    def introduction(self):
        print("Welcome.")
        print("This is a simple list of games that I have beaten in 2025 so far.")

    #   The main menu.
    def main_menu(self):
        
        print("==========================")
        print("MAIN MENU")
        print("==========================")
        print("1. Display all games.")
        print("2. Search for game by console.")
        print("3. Goodbye.")
        
        #   Get terminal user input
        user_order = input("What would you like to do? (PRESS 1-3): ")

        print("==========================")

        if user_order.isnumeric():

             #   Turn terminal input into number for matching
            user_order_conv = int(user_order)
            
            match(user_order_conv):

                #   Display all games
                case(1):
                    self.Display_All(self.glist)                

                #   Search for all games by console
                case(2):
                    self.SearchBy_Console()

                #   Quit program
                case(3):
                    self.Goodbye()

                case _:
                    self.main_menu()
        
        else:

            self.main_menu()

    #   This counts all games
    def countAll(self, glist):

        cntr = 0

        for g in glist:
            cntr = cntr + 1

        return cntr

    #   This displays all games.
    def Display_All(self, glist):

        print("==========================")

        allGamesCntr = self.countAll(glist)

        #   Only display games if there games to display
        if allGamesCntr > 0:

            print("There are: " + str(allGamesCntr) + " games.")

            print("Displaying ALL games: ")

            for g in glist: 
                print ("Name: " + g.gameName + ", Platform: " + g.platform)

        else:
        
            print("There are no games to display.")
        
        print("==========================")

        self.main_menu() 

    #   Counts all xbox games.
    def countXbox(self, glist):

        xboxCntr = 0

        for g in glist:

            if g.platform == "Xbox":

                xboxCntr = xboxCntr + 1

        return xboxCntr

    #   Displays all Xbox games.
    def Display_Xbox_Games(self, glist):

        print("==========================")

        xboxCntr = self.countXbox(glist)

        if xboxCntr > 0:

            print("There are: " + str(xboxCntr) + " XBOX games found.")

            print("Displaying all XBOX games: ")

            for g in glist:

                if g.platform == "Xbox":

                    print ("Name: " + g.gameName + ", Platform: " + g.platform)

        else:

            print("No XBOX games to display.")
        
        print("==========================")

        self.main_menu() 

    #   This counts all Switch games
    def countSwitch(self, glist):

        switchCntr = 0

        for g in glist:
            
            if g.platform == "Nintendo Switch":

                switchCntr = switchCntr + 1

        return switchCntr

    #   This displays all Switch games.
    def Display_Switch_Games(self, glist):

        print("==========================")

        switchCntr = self.countSwitch(glist)

        print("There are " + str(switchCntr) + " Nintendo Switch games found.")

        if switchCntr > 0:

            print("Displaying all NINTENDO SWITCH games:")

            for g in glist: 

                if g.platform == "Nintendo Switch":

                    print ("Name: " + g.gameName + ", Platform: " + g.platform)

        print("==========================")  

        self.main_menu()    

    #   Searches for games according to a console.
    def SearchBy_Console(self):

        print("==========================")

        print("CONSOLE SEARCH MENU:")
        print("1. XBOX")
        print("2. NINTENDO SWITCH")
        print("3. BACK TO MENU")

        user_console = input("What console would you like to search for? (1-3): ")

        if user_console.isnumeric():
            
            user_console_conv = int(user_console)

            match(user_console_conv):

                case(1):
                    self.Display_Xbox_Games(self.glist)

                case(2):
                    self.Display_Switch_Games(self.glist)

                case(3):
                    self.main_menu()

                case _:
                    self.SearchBy_Console()


    #   Quit the program
    def Goodbye(self):

        print("Goodbye.")


        