# Eight-Puzzle
The project involves applying state-space search to a classic problem known as the Eight Puzzle, which is a 3x3 grid containing 8 numbered tiles and one empty or blank cell. 
Here is one possible configuration of the tiles, with the blank cell shown in the middle:
| 1  | 4 | 2 |
| ------------- | ------------- | ------------- |
| 3  |   | 8  |
| 6  | 5  | 7 |

Tiles that are adjacent to the blank cell can move into that position in the grid, and solving the puzzle involves moving the tiles until you reach the following goal state:
|   | 1 | 2 |
| ------------- | ------------- | ------------- |
| 3  | 4 | 5  |
| 6  | 7  | 8 |

In this project, we applied state-space search to solve any valid initial configuration of the Eight Puzzle.

We implemented several classic state-space algorithms:
1. Breadth-First Search: involves always choosing one the untested states that has the smallest depth (i.e., the smallest number of moves from the initial state).
2. Random State-Space Search
3. Depth-First Searcher: involves always choosing one the untested states that has the largest depth (i.e., the largest number of moves from the initial state).
4. Greedy search: uses a heuristic function to estimate the remaining cost needed to get from a given state to the goal state (for the Eight Puzzle, this is just an estimate of how many additional moves are needed). Greedy Search uses this heuristic function when computing the priority of each state, and it selects the next state based on those priorities.
5. A* Search: an informed search algorithm that assigns a priority to each state based on a heuristic function, and that selects the next state based on those priorities. However, when A* assigns a priority to a state, it also takes into account the cost that has already been expended to get to that state (i.e. the number of moves to that state).
More specifically, the priority of a state is computed using the following pseudocode:
```
priority(state) = -1 * (heuristic(state) + num_moves)
```

