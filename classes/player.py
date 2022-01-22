class Player:
    def __init__(self, name, color, pieces=[]):
        self.name = name
        self.color = color
        self.pieces = pieces
        self.move_history = []

    def __repr__(self):
        return str(self.name)

    def __str__(self):
        return repr(self)

    def add_player_piece(self, gained_piece):
        """
        If a player earns pawn promotion add their selected piece to the pieces array.

        :param gained_piece: a piece object
        :return: an updated pieces array
        """
        pass

    def remove_player_piece(self, captured_piece):
        """
        Updates pieces array without captured piece.

        :param captured_piece: a piece object
        :return: an updated pieces array
        """
        pass

    def add_to_history(self, move):
        """
        Adds selected move from the player to their move history.

        :param move: a string of chess notation move
        :return: a new history array with added move
        """
        pass

    def render_history(self):
        """
        Prints the players move history.

        :return: A string which contains the contents of the move array
        """
        pass