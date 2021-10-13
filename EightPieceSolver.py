from EightPieceGame import GameBoard
import copy

'''StateSpaceNode contains one state in the StateSpaceTree'''


class stateNode:

    def __init__(self, state, parent, depth, previous):
        self.state = state
        self.parent = parent
        self.depth = depth
        self.children = []
        self.prevAction = previous


'''StateSpaceTree Holds all necessary states to solve GameBoard'''


class StateSpaceTree:

    def __init__(self, rootState):
        self.root = stateNode(
            state=rootState, parent=None, depth=0, previous=None)


'''gets new state for child node of node'''


def getChildState(arr, action) -> GameBoard:
    newPieces = copy.deepcopy(arr)
    newState = GameBoard(newPieces)
    if action == "w":
        newState.moveUp()
    if action == "a":
        newState.moveLeft()
    if action == "s":
        newState.moveDown()
    if action == "d":
        newState.moveRight()

    return newState


'''expand'''


def expand(currentNode, actions, winstate) -> stateNode:
    q = []
    q.append(currentNode)
    for node in q:
        for action in actions:
            childState = getChildState(node.state.pieces, action)
            childNode = stateNode(childState, node, node.depth + 1, action)
            node.children.append(childNode)
            q.append(childNode)
            if childNode.state.pieces == winstate:
                return childNode


'''Given a Gameboard, winstate, and possible actions returns a solution'''


def Solve(board, winstate, actions) -> list:

    stateSpace = StateSpaceTree(board)
    currentNode = expand(stateSpace.root, actions, winstate)

    solution = []
    while currentNode.parent != None:
        solution.append(currentNode.prevAction)
        currentNode = currentNode.parent

    return list(reversed(solution))
