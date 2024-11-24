import React from "react";
import { useDrag, DragSourceMonitor, DragPreviewImage } from "react-dnd";
import black_bishop from "../assets/black-bishop.svg";
import black_king from "../assets/black-king.svg";
import black_knight from "../assets/black-knight.svg";
import black_pawn from "../assets/black-pawn.svg";
import black_queen from "../assets/black-queen.svg";
import black_rook from "../assets/black-rook.svg";
import white_bishop from "../assets/white-bishop.svg";
import white_king from "../assets/white-king.svg";
import white_knight from "../assets/white-knight.svg";
import white_pawn from "../assets/white-pawn.svg";
import white_queen from "../assets/white-queen.svg";
import white_rook from "../assets/white-rook.svg";


const typeToImage: { [key: string]: string } = {
  R: white_rook,
  N: white_knight,
  B: white_bishop,
  Q: white_queen,
  K: white_king,
  P: white_pawn,
  r: black_rook,
  n: black_knight,
  b: black_bishop,
  q: black_queen,
  k: black_king,
  p: black_pawn,
};

// Define the prop types for the component
type PieceProps = {
  type: string; // e.g., 'P' for Pawn, 'R' for Rook, etc.
  position: [ x: number, y: number ]; // Position could be represented by x, y coordinates
};

const Piece: React.FC<PieceProps> = ({ type, position }) => {
  const [{ isDragging }, drag, preview] = useDrag(() => ({
    type: "PIECE",
    item: { type, position },
    collect: (monitor: DragSourceMonitor) => ({
      isDragging: !!monitor.isDragging(),
    }),
  }));

  return (
    <>
    <DragPreviewImage connect={preview} src={typeToImage[type]} />
    <div
      ref={drag}
      >
        <img
        src={typeToImage[type]}
        alt={type}
        className={`flex items-center  justify-center ${isDragging ? "opacity-50 cursor-move" : ""}`}
      />
    </div>`
    </>
  );
};

export default Piece;