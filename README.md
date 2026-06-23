# AI agent navigation on a grid using a BFS algorithm [Full Guide]

## Overview
A small python simulation project that shows how an AI agent can navigate a 2D environment/grid from the starting point to reach the target while avoiding obstacles. 
It also demonstrates basic graph-search (Breadth-First Search/en 🇫🇷 Parcours en largeur) to find a path through the grid.

## What the code does
### 1) Grid generation
- Creates an `size x size` grid.
- Marks:
  - `S` as the start position (top-left corner)
  - `T` as the target position (bottom-right corner)
  - `O` as randomly placed obstacles

### 2) Agent movement / simulation
- Runs a step-by-step movement where the agent attempts to move toward the target.
- If the next node is the preferred direction it contains an obstacle (`O`), the agent force it self to checking other neighboring node directions.
- While you run the programe, the grid is printed at each step so you can observe the agent’s progression until it reaches `T`.

### 3) Path finding with BFS
- Uses **Breadth-First Search (BFS)** on the grid as a graph.
- BFS explores neighboring nodes (up, down, left, right) + avoiding obstacles.
- When the target is reached, it reconstructs and prints the path from `S` to `T`.

### 4) Clarification of the BFS Algorithm 🔎
- Initialize the queue to empty
- Put the first node in the queue
- **While** the queue is not empty, do:
  - Remove the first node (`popleft`)
  - **If** the removed node is the goal:
    - ✅ Success
  - **Else:**
    - Put its neighbors at the end of the queue

## File structure
- `robot.py` — all logic for grid creation, simulation, and BFS path finding.
- `README.md` — project explanation.

## How to run
1. Make sure you have Python installed (Python 3 recommended).
2. Run:

```bash
python robot.py
```

## Key ideas.
- Using BFS to guarantee the shortest path (in number of moves) on an unweighted grid.
- Simple obstacle avoidance during the simulation.

## Notes / limitations
- BFS provides a correct path when one exists, but the grid size and obstacle placement are randomly generated at runtime.
