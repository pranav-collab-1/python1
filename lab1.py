from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

def bfs(graph,start,destination):
    queue = deque([(start,[start])])
    visited = set([start])


    while queue:
        current_node,path = queue.popleft()
        if current_node == destination:
            return path
        for Next in graph[current_node]:
            if Next not in visited:
                visited.add(Next)
                queue.append((Next,path+[Next]))
    return None

def dfs(graph,start,destination):
    stack = [(start,[start])]
    visited = set()

    while stack:
        current_node,path = stack.pop()
        if current_node == destination:
            return path
        if current_node not in visited:
            visited.add(current_node)
            for Next in reversed(graph[current_node]):
                if Next not in visited: 
                    stack.append((Next,path + [Next]))
    return None
print("BFS Route from A to F:", bfs(graph, 'A', 'F'))
print("DFS Route from A to F:", dfs(graph, 'A', 'F'))
