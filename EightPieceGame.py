'''EightPieceGame:

An implementation of a puzzle game in which the player must reorganise numbers in a grid to match a certain pattern

An abstraction has been made in which the empty piece (represented by a zero) can be moved rather than every other piece. 
this is to reduce complexity for the player as only a direction to move the empty piece must be selected in order to play

'''

import EightPieceSolver
import time


class GameBoard:

    winState = [[1, 2, 3],
                [8, 0, 4],
                [7, 6, 5], ]

    def __init__(self, arr):
        self.pieces = arr
        if arr == None or arr == []:
            self.pieces = [[1, 2, 3],
                           [8, 4, 5],
                           [7, 0, 6], ]

        for i in range(0, 3):
            for j in range(0, 3):
                if self.pieces[i][j] == 0:
                    self.emptyX = j
                    self.emptyY = i

    def show(self) -> None:
        print("-------------")
        for i in range(0, 3):
            print(
                f"| {self.pieces[i][0]} | {self.pieces[i][1]} | {self.pieces[i][2]} |")
            print("-------------")

    def checkWin(self) -> bool:
        return self.pieces == GameBoard.winState

    # Movement Functions

    def moveLeft(self):
        if self.emptyX != 0:
            self.pieces[self.emptyY][self.emptyX] = self.pieces[self.emptyY][self.emptyX - 1]
            self.pieces[self.emptyY][self.emptyX - 1] = 0
            self.emptyX -= 1

    def moveRight(self):
        if self.emptyX != 2:
            self.pieces[self.emptyY][self.emptyX] = self.pieces[self.emptyY][self.emptyX + 1]
            self.pieces[self.emptyY][self.emptyX + 1] = 0
            self.emptyX += 1

    def moveUp(self):
        if self.emptyY != 0:
            self.pieces[self.emptyY][self.emptyX] = self.pieces[self.emptyY - 1][self.emptyX]
            self.pieces[self.emptyY-1][self.emptyX] = 0
            self.emptyY -= 1

    def moveDown(self):
        if self.emptyY != 2:
            self.pieces[self.emptyY][self.emptyX] = self.pieces[self.emptyY + 1][self.emptyX]
            self.pieces[self.emptyY + 1][self.emptyX] = 0
            self.emptyY += 1


def playMove(move, board):
    if move == "w":
        board.moveUp()
    if move == "a":
        board.moveLeft()
    if move == "s":
        board.moveDown()
    if move == "d":
        board.moveRight()


def Main() -> None:
    board = GameBoard([])
    move = ""
    while board.checkWin() != True and move != "solve":  # Main Game Loop
        board.show()
        move = input("Use WASD to move empty piece type 'solve' to finish:\n")
        playMove(move, board)

    if move == "solve":
        solution = EightPieceSolver.Solve(
            board, board.winState, ["w", "a", "s", "d"])
        for step in solution:
            board.show()
            time.sleep(0.75)
            playMove(step, board)

    board.show()
    print("Congrats you win!\n")


if __name__ == "__main__":
    Main()
