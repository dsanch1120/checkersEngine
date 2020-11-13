# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import board
import drawBoard

def play():
    #b = board.Board()

    #b.printSelf()

    d = drawBoard.DrawBoard()
    d.beginGame()
    d.draw()
    test = d.b.possibleMoves(d.currentPlayer)

    print("All done!")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    play()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
