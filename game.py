from classes.board import *
from classes.pieces import *
from classes.communication_module import *
from classes.player import *
from classes.tests import *
from classes.colored import *

print("Welcome to Chess! A simple chess game by tbwebs.")
player_one_name = input("What is your name? ")
print("Welcome ", player_one_name, "! Please enter your move in chess notation (example: b2b4). At any time enter"
                                   " 'help' to bring up a list of commands.\n Good Luck!")

board = Board()
board.set_pieces()


white_pieces = []
black_pieces = []
