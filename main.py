# std imports
from enum import Enum


# piece types
PAWN = 'P'
KNIGHT = 'N'
BISHOP = 'B'
ROOK = 'R'
QUEEN = 'Q'
KING = 'K'


class ChessPiece:
    """ChessPiece class to represent a basic chess piece"""

    def __init__(self, piece_type: int, is_white: bool):
        """Constructor for the ChessPiece class"""
        self.piece_type = piece_type
        self.is_white = is_white

    def __str__(self):
        """String representation of the ChessPiece class"""
        return f"{'W' if self.is_white else 'B'}{self.piece_type}"


class ChessBoard:
    """ChessBoard class to represent a basic chess board"""

    def __init__(self):
        """Constructor for the ChessBoard class"""

        # Create the chess pieces for the white player
        white_pawn = ChessPiece(PAWN, True)
        white_knight = ChessPiece(KNIGHT, True)
        white_bishop = ChessPiece(BISHOP, True)
        white_rook = ChessPiece(ROOK, True)
        white_queen = ChessPiece(QUEEN, True)
        white_king = ChessPiece(KING, True)

        # Create the chess pieces for the black player
        black_pawn = ChessPiece(PAWN, False)
        black_knight = ChessPiece(KNIGHT, False)
        black_bishop = ChessPiece(BISHOP, False)
        black_rook = ChessPiece(ROOK, False)
        black_queen = ChessPiece(QUEEN, False)
        black_king = ChessPiece(KING, False)

        # Create the chess board
        self.board = [
            [
                black_rook,
                black_knight,
                black_bishop,
                black_queen,
                black_king,
                black_bishop,
                black_knight,
                black_rook,
            ],
            [black_pawn for _ in range(8)],
            [None for _ in range(8)],
            [None for _ in range(8)],
            [None for _ in range(8)],
            [None for _ in range(8)],
            [white_pawn for _ in range(8)],
            [
                white_rook,
                white_knight,
                white_bishop,
                white_queen,
                white_king,
                white_bishop,
                white_knight,
                white_rook,
            ],
        ]
    

    def move_piece(self, from_position: tuple, to_position: tuple):
        """Move a piece from one position to another"""
        from_row, from_col = from_position
        to_row, to_col = to_position
        self.board[to_row][to_col] = self.board[from_row][from_col]
        self.board[from_row][from_col] = None
    

    def __str__(self):
        """String representation of the ChessBoard class"""
        return "\n".join(
            [
                " ".join(
                    [str(piece) if piece is not None else ".." for piece in row]
                )
                for row in self.board
            ]
        )

def main():
    chess_board = ChessBoard()
    print(chess_board)
    chess_board.move_piece((1, 0), (2, 0))
    print()
    print(chess_board)

# Run Main Function
if __name__ == "__main__":
    main()
