from algorithm import bfs, dfs, a_star, calculate_path_cost


def create_graph():
    return {
        'A': [('B', 2), ('C', 4)],
        'B': [('A', 2), ('D', 7), ('E', 3)],
        'C': [('A', 4), ('F', 5)],
        'D': [('B', 7), ('G', 2)],
        'E': [('B', 3), ('G', 6)],
        'F': [('C', 5), ('G', 1)],
        'G': [('D', 2), ('E', 6), ('F', 1)]
    }


def get_coordinates():
    return {
        'A': (0, 0),
        'B': (1, 2),
        'C': (2, 0),
        'D': (3, 3),
        'E': (3, 1),
        'F': (4, 0),
        'G': (5, 2)
    }


def main():
    graph = create_graph()
    coordinates = get_coordinates()

    start = 'A'
    goal = 'G'

    print("Traffic Route Optimization using AI Search")
    print("Start:", start)
    print("Destination:", goal)
    print("1. Breadth First Search")
    print("2. Depth First Search")
    print("3. A* Search")

    choice = input("Enter choice (1/2/3): ")

    if choice == '1':
        path = bfs(graph, start, goal)
        algo = "BFS"
    elif choice == '2':
        path = dfs(graph, start, goal)
        algo = "DFS"
    elif choice == '3':
        path = a_star(graph, start, goal, coordinates)
        algo = "A*"
    else:
        print("Invalid choice")
        return

    if path:
        cost = calculate_path_cost(graph, path)
        print("Algorithm Used:", algo)
        print("Path:", " -> ".join(path))
        print("Total Cost:", cost)
    else:
        print("No path found")


if __name__ == "__main__":
    main()