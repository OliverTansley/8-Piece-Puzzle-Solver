import EightPieceGame

'''StateSpaceTree Enumerates all necessary steps to solve GameBoard'''

class stateNode:

    def __init__(self,state):
        self.state = state
        

class StateSpaceTree:

    def __init__(self, rootState):
        self.root = stateNode(rootState)


'''Given a Gameboard and winstate returns a solution'''


def Solve(board, winstate) -> list:
    pass
