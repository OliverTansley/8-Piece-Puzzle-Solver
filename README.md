# Eight-Piece-Solver

## Design Space

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

- branching Factor: 4
- completeness: yes
- optimal: yes
- SearchMethod: Breadth first Search

## Functionality

A breadth first search is used to generate the state space tree. The following actions can be applied to any particular state:

- moveUp
- moveDown
- moveRight
- moveLeft

