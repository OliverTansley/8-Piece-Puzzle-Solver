from EightPieceGame import GameBoard
from MyQueue import MyQueue
import time

'''reimplementations of possible actions'''


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


'''StateSpaceNode contains one state in the StateSpaceTree'''


class stateNode:

    def __init__(self, state, parent, depth, previous):
        self.state = state
        self.parent = parent
        self.depth = depth
        self.children = []
        self.prevAction = previous

    def getChildState(self, action) -> list:
        if action == "w":
            arr = moveUp(self.state.pieces)
        if action == "a":
            arr = moveLeft(self.state.pieces)
        if action == "s":
            arr = moveDown(self.state.pieces)
        if action == "d":
            arr = moveRight(self.state.pieces)
        return arr


'''StateSpaceTree Holds all necessary steps to solve GameBoard'''


class StateSpaceTree:

    def __init__(self, rootState):
        self.root = stateNode(
            state=rootState, parent=None, depth=0, previous=None)


'''expand


currentNode: the initial node of the StateSpaceTree.
actions: list of functions that can be applied to currentNode.state to create a new node.
winstate: the goal state.
'''


def expand(currentNode, actions, winstate) -> stateNode:
    q = []
    q.append(currentNode)

    counter = 0
    while True:
        node = q[counter]  # Get next element in queue
        # for node in q:
        #     print(node.state.pieces)
        time.sleep(5)
        print("--------------------------------")
        counter += 1
        for action in actions:
            # Generate every next state
            childState = node.getChildState(action)
            childNode = stateNode(childState, node, node.depth + 1, action)
            node.children.append(childNode)
            q.append(childNode)
            if childNode.state.pieces == winstate:
                return childNode


'''Given a Gameboard, winstate, and possible actions returns a solution'''


def Solve(board, winstate, actions) -> list:

    stateSpace = StateSpaceTree(board)
    currentNode = stateSpace.root

    currentNode = expand(currentNode, actions, winstate)

    solution = []
    while currentNode.parent != None:
        solution.append(currentNode.prevAction)
        currentNode = currentNode.parent

    return solution
