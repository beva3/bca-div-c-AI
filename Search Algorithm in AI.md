

---

## **1. Basic Problem-Solving Methods**

These are general strategies used to solve problems:

* **Trial and error**: Try different solutions until one works.
* **Rule-based**: Apply fixed rules.
* **Logical reasoning**: Use deduction and inference.

🧠 **Goal**: Move from an **initial state** to a **goal state** through a series of valid steps.

---

## **2. State Space Search**

A **state space** is the set of all possible configurations of a problem.

Each **state** represents a situation, and **actions** move you from one state to another.

---

## **3. Defining Problems as State Space Search**

To define a problem in this way, you need:

* **Initial state**: Where you start
* **Goal state(s)**: The desired outcome
* **Successor function**: Possible actions from each state
* **Path cost** (optional): Cost to move between states

---

## **4. Exhaustive Search**

This method explores **all possible paths**, without using any knowledge or shortcuts.

### 🔹 Breadth-First Search (BFS)

* Explores **level by level**
* Uses a **queue (FIFO)**
* Always finds the **shortest path** (if one exists)

### 🔹 Depth-First Search (DFS)

* Explores **deep into one path** before backtracking
* Uses a **stack (LIFO)**
* May get **stuck in deep paths** or loops if not careful

### 🔹 Bidirectional Search

* Runs **two searches at once**: one from the start, one from the goal
* When they **meet in the middle**, the solution is found
* **Faster** in many cases than BFS or DFS alone

---

## **5. Heuristic Search**

Uses a **heuristic function** to guide the search toward the goal more efficiently.

### 🔹 Hill Climbing

* Always chooses the **best neighbor** based on the heuristic
* May get **stuck in local optima** (not the best overall solution)

### 🔹 Best-First Search

* Uses a **priority queue**
* Selects the node with the **lowest heuristic cost**
* Smarter than Hill Climbing as it can backtrack and explore

### 🔹 A\* Search

* Uses:
  **f(n) = g(n) + h(n)**
  Where:

  * **g(n)** = cost from start to node `n`
  * **h(n)** = estimated cost from `n` to goal
* ✅ Finds the **optimal path**, if the heuristic is good (admissible)

---

