from colored import fg, bg, attr
from classes.board import *
from classes.communication import *
from classes.pieces import *
from classes.player import *
from classes.tests import *


red = fg('red')
reset = attr('reset')
bg_dark_gray = bg('dark_gray')


print(red + 'Welcome to Chess! A simple chess game by tbwebs.' + reset)
player_one_name = input("What is your name? ")
print("Welcome ", player_one_name, "! Please enter your move in chess notation (example: b2b4). At any time enter"
                                   " 'help' to bring up a list of commands.\n Good Luck!")

board = Board()
board.set_pieces()

white_pieces = board.return_pieces("white", board.board)
black_pieces = board.return_pieces("black", board.board)
