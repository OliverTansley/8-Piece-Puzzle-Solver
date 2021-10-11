from EightPieceGame import GameBoard

'''StateSpaceNode contains one state in the StateSpaceTree'''


class stateNode:

    def __init__(self, state, parent, depth, previous):
        self.state = state
        self.parent = parent
        self.depth = depth
        self.children = []
        self.prevAction = previous

    def getChildState(self, action) -> GameBoard:
        return action()


'''StateSpaceTree Holds all necessary steps to solve GameBoard'''


class StateSpaceTree:

    def __init__(self, rootState):
        self.root = stateNode(
            state=rootState, parent=None, depth=0, previous=None)


'''expand
Recursively creates child nodes of 'currentNode' until the node containing 'winstate' is generated, all new nodes are added to the StateSpaceTree

currentNode: the initial node of the StateSpaceTree.
actions: list of functions that can be applied to currentNode.state to create a new node.
winstate: the goal state.
'''


def expand(currentNode, actions, winstate) -> GameBoard:
    for action in actions:
        childState = currentNode.getChildState(action)
        currentNode.children.append(
            stateNode(childState, currentNode, currentNode.depth+1, action))
        if childState != None:
            if childState.pieces != winstate:
                for i in currentNode.children:
                    expand(i, actions, winstate)
            else:
                return childState


'''Given a Gameboard, winstate, and possible actions returns a solution'''


def Solve(board, winstate, actions) -> list:

    stateSpace = StateSpaceTree(board)
    currentNode = stateSpace.root

    expand(currentNode, actions, winstate)

    solution = []
    while currentNode.parent != None:
        solution.append(currentNode.prevAction)
        currentNode = currentNode.parent

    return solution
