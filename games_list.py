
#   13th August 2025.

#   Import everything in the folder.
from games_reader import *
from reader_menu import *

gamesReader = GamesReader()

readerMenu = ReaderMenu(gamesReader.game_objects)
readerMenu.introduction()
readerMenu.main_menu()

