class Piece:
    def __init__(self, piece_name, color):
        self.piece_name = piece_name
        self.color = color
        self.moved = False

    def check_input(self, board_hash, player_input):
        """
        Needs to check the input from the player before analyzing the move for possible moves. Needs to be valid chess
        notation, along with being a possible move within the board.

        :param board_hash: a current state of the board
        :param player_input: a string
        :return: True or False
        """
        pass

    def valid_move_list(self, board_hash, player_input):
        """
        Responsible for creating all the valid moves for whatever instance of the piece is. Will override in child
        classes.

        :param board_hash: current state of the board
        :param player_input: a string
        :return: an array of all valid moves
        """
        pass

    def diagonal_path(self, board_hash, player_input):
        """
        Responsible for making a list of valid move options for diagonal path on the board.

        :param board_hash: a current state of the board
        :param player_input: a string
        :return: an array with valid move options
        """
        pass

    def file_path(self, board_hash, player_input):
        """
        Responsible for making a list of valid move options for the path along the single file on the board.

        :param board_hash: a current state of the board
        :param player_input: a string
        :return:
        """
        pass

    def rank_path(self, board_hash, player_input):
        """
        Responsible for making a list of valid move options for the path along the single rank on the board.

        :param board_hash: a current state of the board
        :param player_input: a string
        :return:
        """
        pass


class Pawn(Piece):
    def __init__(self, piece_name, color):
        super().__init__(piece_name, color)

    def valid_move_list(self, board_hash, player_input):
        """
        Responsible for creating all the valid moves for whatever instance of the piece is. Will override in child
        classes.

        :param board_hash: current state of the board
        :param player_input: a string
        :return: an array of all valid moves
        """
        pass

    def __repr__(self):
        return "\u2659"

    def __str__(self):
        return self.__repr__()


class Rook(Piece):
    def __init__(self,piece_name, color):
        super().__init__(piece_name, color)

    def valid_move_list(self, board_hash, player_input):
        """
        Responsible for creating all the valid moves for whatever instance of the piece is. Will override in child
        classes.

        :param board_hash: current state of the board
        :param player_input: a string
        :return: an array of all valid moves
        """
        pass

    def __repr__(self):
        return "\u2656"

    def __str__(self):
        return self.__repr__()


class Knight(Piece):
    def __init__(self,piece_name, color):
        super().__init__(piece_name, color)

    def valid_move_list(self, board_hash, player_input):
        """
        Responsible for creating all the valid moves for whatever instance of the piece is. Will override in child
        classes.

        :param board_hash: current state of the board
        :param player_input: a string
        :return: an array of all valid moves
        """
        pass

    def __repr__(self):
        return "\u2658"

    def __str__(self):
        return self.__repr__()


class Bishop(Piece):
    def __init__(self, piece_name, color):
        super().__init__(piece_name, color)

    def valid_move_list(self, board_hash, player_input):
        """
        Responsible for creating all the valid moves for whatever instance of the piece is. Will override in child
        classes.

        :param board_hash: current state of the board
        :param player_input: a string
        :return: an array of all valid moves
        """
        pass

    def __repr__(self):
        return "\u2657"

    def __str__(self):
        return self.__repr__()


class Queen(Piece):
    def __init__(self, piece_name, color):
        super().__init__(piece_name, color)

    def valid_move_list(self, board_hash, player_input):
        """
        Responsible for creating all the valid moves for whatever instance of the piece is. Will override in child
        classes.

        :param board_hash: current state of the board
        :param player_input: a string
        :return: an array of all valid moves
        """
        pass

    def __repr__(self):
        return "\u2655"

    def __str__(self):
        return self.__repr__()


class King(Piece):
    def __init__(self, piece_name, color):
        super().__init__(piece_name, color)

    def valid_move_list(self, board_hash, player_input):
        """
        Responsible for creating all the valid moves for whatever instance of the piece is. Will override in child
        classes.

        :param board_hash: current state of the board
        :param player_input: a string
        :return: an array of all valid moves
        """
        pass

    def __repr__(self):
        return "\u2654"

    def __str__(self):
        return self.__repr__()
