import React, { useState, useEffect, useRef } from "react";
import { DndProvider, useDrop, DropTargetMonitor } from "react-dnd";
import { HTML5Backend } from "react-dnd-html5-backend";
import Piece from "./Piece";

type Position = [number, number];
type PieceType = string | null;
type BoardType = PieceType[][];

const initialBoard: BoardType = [
  ["R", "N", "B", "Q", "K", "B", "N", "R"],
  ["P", "P", "P", "P", "P", "P", "P", "P"],
  [null, null, null, null, null, null, null, null],
  [null, null, null, null, null, null, null, null],
  [null, null, null, null, null, null, null, null],
  [null, null, null, null, null, null, null, null],
  ["p", "p", "p", "p", "p", "p", "p", "p"],
  ["r", "n", "b", "q", "k", "b", "n", "r"],
];

const Chessboard: React.FC = () => {
  const [board, setBoard] = useState<BoardType>(initialBoard);
  const ws = useRef<WebSocket | null>(null);

  useEffect(() => {
    ws.current = new WebSocket("ws://localhost:8000/ws");

    ws.current.onmessage = (event) => {
      console.log(event.data);
      const newBoard = JSON.parse(event.data);
      setBoard(newBoard);
    };

    return () => {
      ws.current?.close();
    };
  }, []);

  const movePiece = (fromPosition: Position, toPosition: Position) => {
    const [fromX, fromY] = fromPosition;
    const [toX, toY] = toPosition;
    const piece = board[fromX][fromY];

    const newBoard = board.map((row, rowIndex) =>
      row.map((cell, colIndex) => {
        if (rowIndex === fromX && colIndex === fromY) return null;
        if (rowIndex === toX && colIndex === toY) return piece;
        return cell;
      })
    );

    setBoard(newBoard);
    ws.current?.send(JSON.stringify(newBoard));
  };

  const renderPiece = (position: Position): React.ReactNode => {
    const [x, y] = position;
    const piece = board[x][y];
    return piece ? <Piece type={piece} position={position} /> : null;
  };

  const squares = [];
  for (let row = 0; row < 8; row++) {
    for (let col = 0; col < 8; col++) {
      const isDark = (row + col) % 2 === 1;
      squares.push(
        <Square
          key={`${row}-${col}`}
          position={[row, col]}
          isDark={isDark}
          renderPiece={renderPiece}
          movePiece={movePiece}
        />
      );
    }
  }

  return (
    <DndProvider backend={HTML5Backend}>
      <div className="grid grid-cols-8 gap-0 w-[640px] h-[640px]">{squares}</div>
    </DndProvider>
  );
};

type SquareProps = {
  position: Position;
  isDark: boolean;
  renderPiece: (position: Position) => React.ReactNode;
  movePiece: (fromPosition: Position, toPosition: Position) => void;
};

const Square: React.FC<SquareProps> = ({ position, isDark, renderPiece, movePiece }) => {
  const [{ isOver }, drop] = useDrop<PieceType, void, { isOver: boolean }>({
    accept: "PIECE",
    drop: (item: { position: Position }) => movePiece(item.position, position),
    collect: (monitor: DropTargetMonitor) => ({
      isOver: !!monitor.isOver(),
    }),
  });

  return (
    <div
      ref={drop}
      className={`w-20 h-20 ${isDark ? "bg-gray-800" : "bg-gray-200"} ${isOver ? "bg-yellow-500" : ""}`}
    >
      {renderPiece(position)}
    </div>
  );
};

export default Chessboard;