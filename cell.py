import piece
class Cell:
    givenPiece = None
    x = -1
    y = -1

    def __init__(self, givenPiece, x, y):
        self.givenPiece = givenPiece
        self.x = x
        self.y = y
    def getPiece(self):
        return self.givenPiece