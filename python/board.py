"""CHESS BOARD"""

# local
from pieces import Color, Pawn, Knight, Bishop, Rook, Queen, King

class ChessBoard:
    """ChessBoard class to represent a basic chess board"""

    def __init__(self):
        """Constructor for the ChessBoard class"""

        # Create the chess pieces for the white player
        white_pawn = Pawn(Color.WHITE, "assets/generic/pawn-w.png")
        white_knight = Knight(Color.WHITE, "assets/generic/knight-w.png")
        white_bishop = Bishop(Color.WHITE, "assets/generic/bishop-w.png")
        white_rook = Rook(Color.WHITE, "assets/generic/rook-w.png")
        white_queen = Queen(Color.WHITE, "assets/generic/queen-w.png")
        white_king = King(Color.WHITE, "assets/generic/king-w.png")

        # Create the chess pieces for the black player
        black_pawn = Pawn(Color.BLACK, "assets/generic/pawn-b.png")
        black_knight = Knight(Color.BLACK, "assets/generic/knight-b.png")
        black_bishop = Bishop(Color.BLACK, "assets/generic/bishop-b.png")
        black_rook = Rook(Color.BLACK, "assets/generic/rook-b.png")
        black_queen = Queen(Color.BLACK, "assets/generic/queen-b.png")
        black_king = King(Color.BLACK, "assets/generic/king-b.png")

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

    def get_valid_moves(self, position: tuple) -> list:
        """Get valid moves for the piece at the given position"""
        row, col = position
        piece = self.board[row][col]
        if piece is None:
            return []
        return piece.valid_moves(position, self.board)

    def __str__(self):
        """String representation of the ChessBoard class"""
        return "\n".join(
            [
                " ".join(
                    [str(piece) if piece is not None else "." for piece in row]
                )
                for row in self.board
            ]
        )