from queue import PriorityQueue

def greedy_best_first_search(graph, heuristics, start, target):
    pq = PriorityQueue()
    pq.put((heuristics[start], start, [start]))
    visited = set()
    visited.add(start)

    while not pq.empty():
        h, node, path = pq.get()

        if node == target:
            return path, h

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                pq.put((heuristics[neighbor], neighbor, path + [neighbor]))

    return None, None


# Example Graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

# Heuristic Values
heuristics = {
    'A': 6,
    'B': 4,
    'C': 5,
    'D': 3,
    'E': 2,
    'F': 1,
    'G': 0
}

start = 'A'
target = 'G'

path, h = greedy_best_first_search(graph, heuristics, start, target)

if path:
    print("Path:", " -> ".join(path))
    print("Heuristic value:", h)
else:
    print("Target not found")