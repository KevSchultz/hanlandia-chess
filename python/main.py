# std imports
import argparse
import os
# local
from board import ChessBoard
# 3rd party
import PySimpleGUI as sg

def create_chess_board_layout(chess_board: ChessBoard) -> list:
    """Create the layout for the chess board"""
    board_layout = []
    
    for row_idx, row in enumerate(chess_board.board):
        row_layout = []
        for col_idx, piece in enumerate(row):
            # Alternate colors for chess board pattern
            square_image = 'assets/generic/white_square.png' if (row_idx + col_idx) % 2 == 0 else 'assets/generic/gray_square.png'
            background_color = 'white' if (row_idx + col_idx) % 2 == 0 else 'gray'
            
            button = sg.Button(
                image_filename=piece.image_path if piece else square_image,
                key=f"{row_idx}_{col_idx}",
                pad=(0, 0),
                border_width=0,
                button_color=(background_color, background_color)  # Set background color to match the square
            )
            row_layout.append(button)
        board_layout.append(row_layout)
    
    return board_layout

def update_board_display(window, chess_board: ChessBoard):
    """Update the visual state of the chess board"""
    for row_idx, row in enumerate(chess_board.board):
        for col_idx, piece in enumerate(row):
            key = f"{row_idx}_{col_idx}"
            # Determine the background color based on position
            background_color = 'white' if (row_idx + col_idx) % 2 == 0 else 'gray'
            square_image = 'assets/generic/white_square.png' if (row_idx + col_idx) % 2 == 0 else 'assets/generic/gray_square.png'
            
            # Update both the image and the button color
            window[key].update(
                image_filename=piece.image_path if piece else square_image,
                button_color=(background_color, background_color)
            )

def highlight_valid_moves(window, valid_moves, highlight=True):
    """Highlight or unhighlight valid move positions"""
    for row, col in valid_moves:
        if highlight:
            window[f"{row}_{col}"].update(button_color=('black', 'yellow'))
        else:
            # Reset to original chess board pattern
            background_color = 'white' if (row + col) % 2 == 0 else 'gray'
            square_image = 'assets/generic/white_square.png' if (row + col) % 2 == 0 else 'assets/generic/gray_square.png'
            window[f"{row}_{col}"].update(button_color=(background_color, background_color), image_filename=square_image)

def main():
    parser = argparse.ArgumentParser(description="Chess game in GUI or text mode")
    parser.add_argument('--mode', choices=['gui', 'text'], default='gui', 
                       help='Mode to run the chess game')
    args = parser.parse_args()
    
    chess_board = ChessBoard()
    
    if args.mode == 'gui':
        # Create the layout
        board_layout = create_chess_board_layout(chess_board)
        layout = board_layout
        
        # Create the window
        window = sg.Window("Hanlandia Chess Game", layout, finalize=True)
        
        selected_piece = None
        valid_moves = []
        
        while True:
            event, values = window.read()
            
            if event in (sg.WIN_CLOSED, "Exit"):
                break
            
            if isinstance(event, str) and "_" in event:
                row, col = map(int, event.split("_"))
                
                if selected_piece is None:
                    # Selecting a piece
                    if chess_board.board[row][col] is not None:
                        selected_piece = (row, col)
                        valid_moves = chess_board.get_valid_moves((row, col))
                        highlight_valid_moves(window, valid_moves)
                        window.refresh()  
                else:
                    # Moving a selected piece
                    if (row, col) in valid_moves:
                        # Make the move
                        chess_board.move_piece(selected_piece, (row, col))
                        update_board_display(window, chess_board)
                        selected_piece = None
                        valid_moves = []
                        window.refresh()
                
        
        window.close()
    
    else:
        # Text mode implementation remains the same
        print("Running in text mode")
        print(chess_board)
        while True:
            try:
                move = input("Enter move (format: from_row from_col to_row to_col): ")
                if move.lower() == 'quit':
                    break
                
                from_row, from_col, to_row, to_col = map(int, move.split())
                chess_board.move_piece((from_row, from_col), (to_row, to_col))
                print(chess_board)
            
            except ValueError:
                print("Invalid input format. Use: from_row from_col to_row to_col")
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    main()