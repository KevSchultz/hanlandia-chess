"""CHESS PIECES"""
# std imports
from enum import Enum


# Color Enum
class Color(Enum):
    """Color Enum to represent the color of a chess piece"""
    WHITE = 1
    BLACK = 2


def color_string(text: str, color: Color) -> str:
    """Return the text wrapped with the corresponding ANSI color code."""
    colors = {
        Color.BLACK: '\033[30m',
        Color.WHITE: '\033[97m',
    }
    reset = '\033[0m'

    return f"{colors.get(color, reset)}{text}{reset}"


class ChessPiece:
    """ChessPiece class to represent a basic chess piece"""

    def __init__(self, color: Color, image_path: str):
        """Constructor for the ChessPiece class"""
        self.color = color
        self.image_path = image_path

    def valid_moves(self, position, board):
        """Method to be overridden by each specific piece"""
        raise NotImplementedError("This method should be overridden by subclasses")


class Pawn(ChessPiece):
    """Pawn class to represent a pawn chess piece"""

    def __str__(self):
        """String representation of the Pawn class"""
        return color_string("P", self.color)

    def valid_moves(self, position, board):
        row, col = position
        moves = []
        direction = -1 if self.color == Color.WHITE else 1

        # Move forward
        if board[row + direction][col] is None:
            moves.append((row + direction, col))
            # Move two squares forward from starting position
            if (self.color == Color.WHITE and row == 6) or (self.color == Color.BLACK and row == 1):
                if board[row + 2 * direction][col] is None:
                    moves.append((row + 2 * direction, col))

        # Capture diagonally
        for dc in [-1, 1]:
            if 0 <= col + dc < 8 and board[row + direction][col + dc] is not None and board[row + direction][col + dc].color != self.color:
                moves.append((row + direction, col + dc))

        return moves


class King(ChessPiece):
    """King class to represent a king chess piece"""

    def __str__(self):
        """String representation of the King class"""
        return color_string("K", self.color)

    def valid_moves(self, position, board):
        row, col = position
        moves = []
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                if board[new_row][new_col] is None or board[new_row][new_col].color != self.color:
                    moves.append((new_row, new_col))

        return moves


class Queen(ChessPiece):
    """Queen class to represent a queen chess piece"""

    def __str__(self):
        """String representation of the Queen class"""
        return color_string("Q", self.color)

    def valid_moves(self, position, board):
        row, col = position
        moves = []
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            while 0 <= new_row < 8 and 0 <= new_col < 8:
                if board[new_row][new_col] is None:
                    moves.append((new_row, new_col))
                elif board[new_row][new_col].color != self.color:
                    moves.append((new_row, new_col))
                    break
                else:
                    break
                new_row += dr
                new_col += dc

        return moves


class Bishop(ChessPiece):
    """Bishop class to represent a bishop chess piece"""

    def __str__(self):
        """String representation of the Bishop class"""
        return color_string("B", self.color)

    def valid_moves(self, position, board):
        row, col = position
        moves = []
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            while 0 <= new_row < 8 and 0 <= new_col < 8:
                if board[new_row][new_col] is None:
                    moves.append((new_row, new_col))
                elif board[new_row][new_col].color != self.color:
                    moves.append((new_row, new_col))
                    break
                else:
                    break
                new_row += dr
                new_col += dc

        return moves


class Knight(ChessPiece):
    """Knight class to represent a knight chess piece"""

    def __str__(self):
        """String representation of the Knight class"""
        return color_string("N", self.color)

    def valid_moves(self, position, board):
        row, col = position
        moves = []
        directions = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                if board[new_row][new_col] is None or board[new_row][new_col].color != self.color:
                    moves.append((new_row, new_col))

        return moves


class Rook(ChessPiece):
    """Rook class to represent a rook chess piece"""

    def __str__(self):
        """String representation of the Rook class"""
        return color_string("R", self.color)

    def valid_moves(self, position, board):
        row, col = position
        moves = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            while 0 <= new_row < 8 and 0 <= new_col < 8:
                if board[new_row][new_col] is None:
                    moves.append((new_row, new_col))
                elif board[new_row][new_col].color != self.color:
                    moves.append((new_row, new_col))
                    break
                else:
                    break
                new_row += dr
                new_col += dc

        return moves