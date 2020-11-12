import pygame
import board

class DrawBoard:
    size = 0
    boardLength = 0
    currentPlayer = 0
    white, black, red = (255, 255, 255), (0, 0, 0), (255, 0, 0)
    gameDisplay = pygame.display.set_mode((800, 600))
    b = None

    def __init__(self):
        self.size = 65
        self.boardLength = 8
        self.gameDisplay.fill(self.white)
        self.b = board.Board()


    def beginGame(self):
        pygame.init()

    def draw(self):
        cnt = 0
        for i in range(1, self.boardLength+1):
            for z in range(1, self.boardLength+1):
                if cnt % 2 == 0:
                    pygame.draw.rect(self.gameDisplay, self.red, [self.size*z, self.size*i, self.size, self.size])
                else:
                    pygame.draw.rect(self.gameDisplay, self.black, [self.size * z, self.size * i, self.size, self.size])
                cnt += 1
                self.drawCircle((i*self.size) + (self.size / 2), z*self.size + (self.size / 2), self.b.layout[i - 1][z - 1].givenPiece.icon)
            cnt -= 1
        pygame.draw.rect(self.gameDisplay, self.black, [self.size, self.size, self.boardLength*self.size, self.boardLength*self.size], 1)
        pygame.display.update()

    def drawCircle(self, x, y, col):
        if col == 'B':
            pygame.draw.circle(self.gameDisplay, self.white, [y, x], 25)
        elif col == 'R':
            pygame.draw.circle(self.gameDisplay, self.red, [y, x], 25)
        else:
            return

    def quitGame(self):
        pygame.quit()
        quit()

