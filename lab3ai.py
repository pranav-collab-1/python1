import heapq

graph = {
    'GNT': ['VJA', 'RJY'],
    'VJA': ['TPTY', 'ELURU'],
    'RJY': ['HYD'],
    'VSKP': [],
    'ELURU': ['GNT', 'VZN'],
    'HYD': [],
    'VZN': []
}

heuristics = {
    'GNT': 6,
    'VJA': 4,
    'RJY': 5,
    'VSKP': 7,
    'ELURU': 2,
    'HYD': 8,
    'VZN': 0,
    'TPTY': 3
}

def greedy_best_first_search(graph, heuristics, start, goal):
    frontier = []
    heapq.heappush(frontier, (heuristics[start], start))
    visited = set()
    parent_map = {start: None}

    while frontier:
        current_h, current_node = heapq.heappop(frontier)

        if current_node in visited:
            continue

        visited.add(current_node)

        if current_node == goal:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = parent_map[current_node]
            return path[::-1]

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                parent_map[neighbor] = current_node
                heapq.heappush(frontier, (heuristics[neighbor], neighbor))

    return None

path = greedy_best_first_search(graph, heuristics, 'GNT', 'VZN')
print("Path found:", path)
