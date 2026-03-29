# Traffic Route Optimization Simulator using AI Search Algorithms

## Overview

This project implements a Traffic Route Optimization Simulator using classical Artificial Intelligence search algorithms. The objective is to find the best route between a start location and a destination in a city while considering traffic conditions represented as costs.

The city is modeled as a graph where intersections are nodes and roads are edges with associated traffic costs. The project compares uninformed and informed search techniques to highlight their effectiveness in real-world routing problems.

---

## Features

* Implementation of BFS, DFS, and A* search algorithms
* Graph-based city representation
* Traffic-aware route cost calculation
* Command-line interface (CLI) based execution
* Displays optimal path and total cost
* Comparison between different search strategies

---

## Project Structure

```
Traffic Route Optimization Simulator/

── main.py          # Handles graph creation, user input, and execution  
── algorithms.py    # Contains BFS, DFS, A* implementations  
── README.md        # Project overview  
── report.pdf       # Project report  
```

---

## Installation

1. Clone or download the project files.

2. Navigate to the project directory:

```
cd "Traffic Route Optimization Simulator"
```

3. Ensure Python 3.x is installed on your system.

No external libraries are required.

---

## Usage

Run the program using:

```
python main.py
```

### Input Format

* Select one of the following algorithms:

  * 1 → Breadth First Search (BFS)
  * 2 → Depth First Search (DFS)
  * 3 → A* Search

The start node and destination node are predefined in the program.

---

## Output

The program displays:

* Algorithm used
* Path from start to destination
* Total traffic cost of the path

### Example Output

```
Traffic Route Optimization using AI Search
Start: A
Destination: G
1. Breadth First Search
2. Depth First Search
3. A* Search
Enter choice (1/2/3): 3

Algorithm Used: A*
Path: A -> C -> F -> G
Total Cost: 10
```

---

## Algorithms Used

### Breadth First Search (BFS)

BFS is an uninformed search algorithm that explores nodes level by level.

In this project:

* Finds the shortest path based on number of steps
* Does not consider traffic cost during search
* May not produce the optimal route in weighted graphs

---

### Depth First Search (DFS)

DFS explores a path as deeply as possible before backtracking.

In this project:

* Used for exploration and comparison
* Does not guarantee shortest or least-cost path

---

### A* Search Algorithm

A* is an informed search algorithm that uses a heuristic.

In this project:

* Combines actual cost and heuristic estimate
* Uses Manhattan distance as heuristic
* Produces the most optimal route based on traffic cost

---

## Problem Representation

* Locations → Nodes
* Roads → Edges
* Traffic conditions → Edge weights
* Start location → Initial state
* Destination → Goal state

---

## Conclusion

This project demonstrates how AI search algorithms can be applied to real-world problems such as traffic route optimization. The comparison between BFS, DFS, and A* highlights why informed search algorithms are preferred for decision-making in cost-sensitive environments.

---

## Learning Outcomes

Through this project, I gained a better understanding of:

* Graph-based problem modeling
* Uninformed vs informed search techniques
* Heuristic-based optimization
* Path cost evaluation
* Modular Python programming

---

## Challenges Faced

Some challenges encountered during development:

* Designing an effective graph representation
* Implementing A* with correct cost and heuristic handling
* Comparing algorithm performance meaningfully
* Ensuring clean and readable code structure

---

## Future Improvements

This project can be enhanced by:

* Allowing user-defined start and destination nodes
* Adding real-time or dynamic traffic updates
* Visualizing routes graphically
* Expanding the city map with more locations

---

## Author Note

This project was developed as part of an AI/ML Bring Your Own Project (BYOP) to demonstrate the application of search algorithms in solving real-world routing and optimization problems.

---
