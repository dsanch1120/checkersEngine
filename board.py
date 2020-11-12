import cell
import piece


class Board:
    layout = []

    def __init__(self):
        self.makeBoard()

    def makeBoard(self):
        for i in range(8):
            tempList = []
            for j in range(8):
                if i == 0 or i == 2:
                    if j % 2 == 1:
                        tempList += [cell.Cell(piece.Piece('B', j, i), j, i)]
                    else:
                        tempList += [cell.Cell(piece.Piece('X', j, i), j, i)]
                elif i == 1:
                    if j % 2 == 0:
                        tempList += [cell.Cell(piece.Piece('B', j, i), j, i)]
                    else:
                        tempList += [cell.Cell(piece.Piece('X', j, i), j, i)]
                elif i == 3 or i == 4:
                    tempList += [cell.Cell(piece.Piece('X', j, i), j, i)]
                elif i == 5 or i == 7:
                    if j % 2 == 0:
                        tempList += [cell.Cell(piece.Piece('R', j, i), j, i)]
                    else:
                        tempList += [cell.Cell(piece.Piece('X', j, i), j, i)]
                else:
                    if j % 2 == 1:
                        tempList += [cell.Cell(piece.Piece('R', j, i), j, i)]
                    else:
                        tempList += [cell.Cell(piece.Piece('X', j, i), j, i)]
            self.layout += [tempList]

    def possibleMoves(self, cp):
        yDirection = -1
        moveable = 'R'
        if cp == 0:
            yDirection = 1
            moveable = 'B'

        copy = self.layout

        for i in self.layout:
            jCounter = 0
            for j in i:
                if j.givenPiece is None or j.givenPiece.icon != moveable:
                    jCounter += 1
                    continue
                else:
                    xDirection = 1
                    r = 2
                    if jCounter % 2 == 1:
                        xDirection = -1
                    if jCounter == 0 or jCounter == 7:
                        r = 1
                    for k in range(r):
                        if self.layout[j.y + yDirection][j.x + xDirection].givenPiece.icon == 'X':
                            # Add this move to the board
                            print("No Piece", j.x, " ", j.y)
                        elif self.layout[j.y + yDirection][j.x + xDirection].givenPiece.icon == moveable:
                            jCounter += 1
                            continue
                        else:
                            print("Red Piece")
                        xDirection *= -1
                jCounter += 1

    def printSelf(self):
        for i in range(8):
            for j in range(8):
                print(self.layout[i][j].givenPiece.icon, end="")
            print()
