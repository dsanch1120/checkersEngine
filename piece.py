class Piece:
    # Global Variables
    icon = ' '
    x = -1
    y = -1

    def __init__(self, icon, x, y):
        self.icon = icon
        self.x = x
        self.y = y

    def getCoordinates(self):
        return [self.x, self.y]

    def getIcon(self):
        return self.icon