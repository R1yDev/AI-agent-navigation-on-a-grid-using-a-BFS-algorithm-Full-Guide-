# 🤖 AI Agent Navigation on a Grid using BFS [Full Guide]

## 📖 Overview
A small Python simulation project that shows how an AI agent can navigate a 2D environment/grid from a starting point to reach a target while avoiding obstacles. It demonstrates basic graph-search — **Breadth-First Search** (FR: *Parcours en largeur* 🇫🇷) — to find a path through the grid.

---

## ⚙️ What the code does

### 1️⃣ Grid generation
- Creates a `size x size` grid.
- Marks:
  - `S` → start position (top-left corner)
  - `T` → target position (bottom-right corner)
  - `O` → randomly placed obstacles

### 2️⃣ Agent movement / simulation
- Runs a step-by-step movement where the agent attempts to move toward the target.
- If the preferred direction is blocked by an obstacle (`O`), the agent checks other neighboring directions instead.
- The grid is printed at each step, so you can watch the agent's progress until it reaches `T`.

### 3️⃣ Path finding with BFS
- Uses **Breadth-First Search (BFS)** on the grid as a graph.
- BFS explores neighboring nodes (up, down, left, right) while avoiding obstacles.
- Once the target is reached, it reconstructs and prints the path from `S` to `T`.

### 4️⃣ Clarification of the BFS Algorithm 🔎

```text
Initialize the queue to empty
Put the first node in the queue

While the queue is not empty:
    Remove the first node (popleft)
    If the removed node is the goal:
        ✅ Success
    Else:
        Put its neighbors at the end of the queue
```

---

## 📂 File structure
| File | Purpose |
|---|---|
| `robot.py` | All logic for grid creation, simulation, and BFS path finding |
| `README.md` | Project explanation |

## ▶️ How to run
1. Make sure Python is installed (Python 3 recommended).
2. Run:

```bash
python robot.py
```

## 💡 Key ideas
- Using BFS to guarantee the shortest path (in number of moves) on an unweighted grid.
- Simple obstacle avoidance during the simulation.

## ⚠️ Notes / limitations
- BFS provides a correct path when one exists, but grid size and obstacle placement are randomized at runtime, so results vary between runs.
