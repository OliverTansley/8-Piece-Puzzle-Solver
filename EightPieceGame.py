'''EightPieceGame'''

import EightPieceSolver
from time import sleep


'''GameBoard Object
Represents the puzzle game through a 2D array and implements functionality required to play.

show: Displays the current state of the puzzle to the terminal.
checkwin: determines if the game has been solved.
movement: alters the contents of the puzzle to represent a single move.

Constructor can take in array to build new GameBoard with predetermined contents used for solver.

Location of empty piece is stored to improve efficiency (index's dont have to be found every time)
'''


class GameBoard:

    winState = [[1, 2, 3],
                [8, 0, 4],
                [7, 6, 5], ]

    def __init__(self, arr):
        if arr:
            self.pieces = arr
            # Locate the empty peice
            for i in range(0, 3):
                for j in range(0, 3):
                    if self.pieces[i][j] == 0:
                        self.emptyX = j
                        self.emptyY = i
        else:
            self.emptyX = 1
            self.emptyY = 2
            self.pieces = [[1, 2, 3],
                           [8, 4, 5],
                           [7, 0, 6], ]

    def show(self) -> None:
        print("-------------")
        for i in range(0, 3):
            print(
                f"| {self.pieces[i][0]} | {self.pieces[i][1]} | {self.pieces[i][2]} |")
            print("-------------")

    def checkWin(self) -> bool:
        return self.pieces == GameBoard.winState

    ''' Movement Functions '''

    def moveLeft(self) -> None:
        if self.emptyX != 0:
            self.pieces[self.emptyY][self.emptyX] = self.pieces[self.emptyY][self.emptyX - 1]
            self.pieces[self.emptyY][self.emptyX - 1] = 0
            self.emptyX -= 1

    def moveRight(self) -> None:
        if self.emptyX != 2:
            self.pieces[self.emptyY][self.emptyX] = self.pieces[self.emptyY][self.emptyX + 1]
            self.pieces[self.emptyY][self.emptyX + 1] = 0
            self.emptyX += 1

    def moveUp(self) -> None:
        if self.emptyY != 0:
            self.pieces[self.emptyY][self.emptyX] = self.pieces[self.emptyY - 1][self.emptyX]
            self.pieces[self.emptyY-1][self.emptyX] = 0
            self.emptyY -= 1

    def moveDown(self) -> None:
        if self.emptyY != 2:
            self.pieces[self.emptyY][self.emptyX] = self.pieces[self.emptyY + 1][self.emptyX]
            self.pieces[self.emptyY + 1][self.emptyX] = 0
            self.emptyY += 1


'''playMove: maps input action to an intended board move'''


def playMove(move, board) -> None:
    if move.lower() == "w":
        board.moveUp()
    if move.lower() == "a":
        board.moveLeft()
    if move.lower() == "s":
        board.moveDown()
    if move.lower() == "d":
        board.moveRight()


'''Main: Implements game loop, allowing for the user to input a move or for the AI to solve the puzzle from the current state.'''


def Main() -> None:
    board = GameBoard([])
    move = ""
    while board.checkWin() != True and move != "solve":  # Main Game Loop
        board.show()
        move = input("Use WASD to move empty piece type 'solve' to finish:\n")
        playMove(move, board)

    if move.lower() == "solve":  # Call AI to solve
        solution = EightPieceSolver.Solve(
            board, board.winState, ["w", "a", "s", "d"])
        for step in solution:
            board.show()
            sleep(0.75)
            playMove(step, board)

    board.show()
    print("Congrats you win!")


if __name__ == "__main__":
    Main()
