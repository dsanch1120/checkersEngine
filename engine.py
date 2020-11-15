import copy

import treelib
from treelib import node, tree

import board
import drawBoard


class Engine:

    def __init__(self):
        self.tree = tree.Tree()

    def defineRoot(self, b):
        self.tree.create_node(b, identifier=b.id)

    def arrToBoard(self, arr):
        output = []
        for i in arr:
            b = board.Board()
            b.layout = i
            output += [copy.deepcopy(b)]
        return copy.deepcopy(output)

    def giveBirth(self, level, arr):
        counter = 1
        for i in arr:
            self.tree.create_node()

    def ctrl(self):
        self.d = drawBoard.DrawBoard()
        self.d.beginGame()
        # d.draw()
        test = self.d.b.possibleMoves(self.d.currentPlayer)
        self. d.b.layout = test[6]
        self. d.draw()
        test2 = self.arrToBoard(test)
        print(test2)
        self.defineRoot(self.d.b)
        print("All done!")