import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Chessboard from './components/ChessBoard'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <Chessboard />
    </>
  )
}

export default App
