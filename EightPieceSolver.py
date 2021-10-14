'''EightPieceSolver'''


from EightPieceGame import GameBoard
from copy import deepcopy


'''StateNode: Contains one state of the StateSpaceTree

state: The current state of the world
parent: The previous state of the world
depth: The depth of the node in the StateSpaceTree
'''


class StateNode:

    # Constructor
    def __init__(self, state, parent, depth, previous):
        self.state = state
        self.parent = parent
        self.depth = depth
        self.children = []
        self.prevAction = previous


'''StateSpaceTree: Contains the Root node of the StateSpaceTree'''


class StateSpaceTree:

    # Constructor
    def __init__(self, rootState):
        self.root = StateNode(
            state=rootState, parent=None, depth=0, previous=None)


'''getChildState: Applys an action to the current state returning a new world state'''


def getChildState(state, action) -> GameBoard:
    newPieces = deepcopy(state.pieces)
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


'''expand: Constructs full StateSpaceTree using breadthFirstSearch and returns node containing winstate'''


def expand(StateSpaceTree, actions, winstate) -> StateNode:
    q = []
    q.append(StateSpaceTree)
    for node in q:
        for action in actions:
            childState = getChildState(node.state, action)
            childNode = StateNode(childState, node, node.depth + 1, action)
            node.children.append(childNode)
            q.append(childNode)
            if childNode.state.pieces == winstate:
                return childNode


'''Given a Gameboard, desired state, and list of possible actions returns a solution
This function can be thought of as the Agent.
'''


def Solve(board, winstate, actions) -> list:

    stateSpace = StateSpaceTree(board)
    currentNode = expand(stateSpace.root, actions, winstate)

    solution = []
    while currentNode.parent != None:
        solution.append(currentNode.prevAction)
        currentNode = currentNode.parent

    return list(reversed(solution))
