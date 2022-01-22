
import random
from classes.pieces import *
from classes.colored import *
BOARD_SIZE = 64


class Board:
    def __init__(self):
        """
        Initialize the board with the pieces and board size which defaults at 64. Implement instances of the pieces in
         order to set up the board.

        Will also create a board hash in this class for easier lookup with the string inputs from the player.
        """
        self.board = [["  " for _ in range(8)] for _ in range(8)]
        self.board_hash = [[[random.randint(1, 2 ** 64 - 1) for _ in range(12)] for _ in range(8)] for _ in range(8)]

    def piece_indexing(self, piece_name):
        """
        Helper function to identify piece for hashing. Uppercase if white pieces and lowercase is black.

        :param piece_name: the pieces title
        :return: an integer
        """
        if piece_name == "Pawn":
            return 0
        if piece_name == "Rook":
            return 1
        if piece_name == "Knight":
            return 2
        if piece_name == "Bishop":
            return 3
        if piece_name == "Queen":
            return 4
        if piece_name == "King":
            return 5
        if piece_name == "pawn":
            return 6
        if piece_name == "rook":
            return 7
        if piece_name == "knight":
            return 8
        if piece_name == "bishop":
            return 9
        if piece_name == "queen":
            return 10
        if piece_name == "king":
            return 11
        else:
            return -1

    def compute_hash(self, board):
        """
        Computes the hash number for the board

        :param board: the board array
        :return: an integer hash number
        """
        h = 0
        for i in range(8):
            for j in range(8):
                if board[i][j] != "  ":
                    piece = self.piece_indexing(board[i][j])
                    h ^= self.board_hash[i][j][piece]
        return h

    def set_pieces(self):
        """
        Sets up the board initially to start the game.

        :return: A new board with pieces in initial position for the game
        """
        self.board[0][0] = Rook("rook", "black")
        self.board[0][1] = Knight("knight", "black")
        self.board[0][2] = Bishop("bishop", "black")
        self.board[0][3] = Queen("queen", "black")
        self.board[0][4] = King("king", "black")
        self.board[0][5] = Bishop("bishop", "black")
        self.board[0][6] = Knight("knight", "black")
        self.board[0][7] = Rook("rook", "black")
        self.board[7][0] = Rook("Rook", "white")
        self.board[7][1] = Knight("Knight", "white")
        self.board[7][2] = Bishop("Bishop", "white")
        self.board[7][3] = Queen("Queen", "white")
        self.board[7][4] = King("King", "white")
        self.board[7][5] = Bishop("Bishop", "white")
        self.board[7][6] = Knight("Knight", "white")
        self.board[7][7] = Rook("Rook", "white")

        for file in range(8):
            self.board[1][file] = Pawn("pawn", "black")

        for file in range(8):
            self.board[6][file] = Pawn("Pawn", "white")

    def return_pieces(self, color, board):
        """
        Return's a list of all the active pieces on the board
        :param color: color of pieces you want to find, a string
        :param board: a current state of the board object
        :return: an array of all the color pieces
        """
        all_pieces = []

        for rank in range(8):
            for file in range(8):
                if board[rank][file] != "  ":
                    if board[rank][file].color == color:
                        all_pieces.append(board[rank][file])
        return all_pieces

    def render_board(self):
        """
        Will display the board in a readable format on the console.

        :return: A string of the board array.
        """
        rank = 8
        render = "Current Board State:\n"
        for rank in range(8)

    def move_piece(self, board, input_in_chess_notation):
        """
        Will move the selected piece from its current location to the desired location. Will need to implement helper
        functions in order determine if captures need to take place or not. Will also need to update the board.

        :param board: the array of the board
        :param input_in_chess_notation: a string of inputted chess notation
        :return: an updated board
        """
        pass

    def update_board(self, edited_board):
        """
        Helper function to update the board state whenever it's needed in another function.

        :param edited_board: the changed board
        :return: an updated board
        """
        pass

    def find_space(self, coordinates):
        """
        Will return the space of the inputted coordinates.

        :param coordinates: an array of two numbers representing the numerical board coordinates
        :return: the contents of the space assigned to the coordinates
        """
        pass

    def checkmate(self, board, turn_color):
        """
        Evaluates the current board state if a player is in check, checkmate, or neither and will return false.

        :param board: current board state
        :param turn_color: either the current turn color or current player
        :return: False, "check", or "checkmate"
        """
        pass

    def en_passant(self, board, move_input, turn_color):
        """
        Will need to analyze board and piece positions in order to see if an en passant is possible.

        :param board: a current state of the board
        :param move_input: a string
        :param turn_color: either the current turn color or current player
        :return: True or False
        """
        pass

    def castle(self, board, move_input, turn_color):
        """
        Will need to analyze the board and piece positions in order to see if a castle is possible. Will need to figure
        out how to distinguish between king and queen side castles.

        :param board: a current state of the board
        :param move_input: a string
        :param turn_color: either the current turn color or current player
        :return: True or false
        """
        pass

    def __repr__(self):
        # will contain the "render_board" function
        pass

    def __str__(self):
        pass
        # return repr(self)
