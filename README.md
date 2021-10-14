# Eight-Piece-Solver

The AI evaluates all possible states of the puzzle game starting from the current state, this ensures that the solution with the least steps required will be found first, as no combination of steps is missed.

The states are stored in a state space tree which once constructed can be traversed to retrieve the list of instructions required to solve the current state of the Puzzle.

## Design Dimensions

- Modularity: flat
- Planning Horizon: indefinite
- Representation: Explicit states
- Computational limits: bounded rationality
- learning: knowledge is given
- Uncertainty: deterministic
- Preference: goal based
- Number of agents: 1
- Interaction: offline

## StateSpaceTree

- SearchMethod: Breadth first Search
- branching Factor: 4
- completeness: yes
- optimal: yes

## Functionality

A breadth first search is used to generate the state space tree. The following actions can be applied to any particular state:

- moveUp
- moveDown
- moveRight
- moveLeft

## Efficiency

- Time Complexity is order O(4^(d)), where d is the depth of the solution.
- Space Complexity every node is kept in memory: O(4^d-1) explored, so space complexity is O(4^d).
