from collections import deque
import heapq


# Breadth First Search
def bfs(graph, start, goal):
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor, cost in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return None


# Depth First Search
def dfs(graph, start, goal):
    stack = [[start]]
    visited = set()

    while stack:
        path = stack.pop()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor, cost in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                stack.append(new_path)

    return None


# Heuristic function for A*
def heuristic(node, goal, coordinates):
    x1, y1 = coordinates[node]
    x2, y2 = coordinates[goal]
    return abs(x1 - x2) + abs(y1 - y2)


# A* Search Algorithm
def a_star(graph, start, goal, coordinates):
    open_list = []
    heapq.heappush(open_list, (0, start))

    came_from = {}
    g_cost = {start: 0}

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            return reconstruct_path(came_from, current)

        for neighbor, cost in graph[current]:
            new_cost = g_cost[current] + cost

            if neighbor not in g_cost or new_cost < g_cost[neighbor]:
                g_cost[neighbor] = new_cost
                f_cost = new_cost + heuristic(neighbor, goal, coordinates)
                heapq.heappush(open_list, (f_cost, neighbor))
                came_from[neighbor] = current

    return None


# Path reconstruction
def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path


# Calculate total cost of path
def calculate_path_cost(graph, path):
    total_cost = 0
    for i in range(len(path) - 1):
        for neighbor, cost in graph[path[i]]:
            if neighbor == path[i + 1]:
                total_cost += cost
                break
    return total_cost