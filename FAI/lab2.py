import heapq
graph={'Hyd':{'War':75,'Nag':140,'Pune':118},
       'war':{'Hyd':75,'Niz':71},
       'Niz': {'War': 71, 'Nag': 151},
       'Nag': {'Hyd': 140, 'Niz': 151, 'Agra': 99, 'Kanpur': 80},
    'Pune': {'Hyd': 118, 'Aur': 111},
    'Aur': {'Pune': 111, 'Bhopal': 70},
    'Bhopal': {'Aur': 70, 'Indore': 75},
    'Indore': {'Bhopal': 75, 'Jabalpur': 120},
    'Jabalpur': {'Indore': 120, 'Kanpur': 146, 'Gwalior': 138},
    'Kanpur': {'Nag': 80, 'Jabalpur': 146, 'Gwalior': 97},
    'Agra': {'Nag': 99, 'Delhi': 211},
    'Gwalior': {'Kanpur': 97, 'Jabalpur': 138, 'Delhi': 101},
    'Delhi': {'Agra': 211, 'Gwalior': 101}
}
heuristic={'Hyd':366,'War':374,'Niz':380,'Nag':253,'Pune': 329,
             'Aurangabad': 244, 'Bhopal': 241, 'Indore': 242, 'Jabalpur': 160, 'Kanpur': 193,
             'Agra': 176, 'Gwalior': 100, 'Delhi': 0}

def astar(start, goal):
    open_list, best_g, expanded = [(heuristic[start], start, [start], 0)], {}, 0
    while open_list:
        f, node, path, g = heapq.heappop(open_list)
        if node in best_g and best_g[node] <= g:    
            continue
        best_g[node] = g
        expanded += 1
        if node == goal:
            return path, g, expanded
        for nbr, cost in graph.get(node, {}).items():
            new_g = g + cost
            if nbr not in best_g or new_g < best_g[nbr]:
                                heapq.heappush(open_list, (new_g + heuristic[nbr], nbr, path + [nbr], new_g))
    return None, float('inf'), expanded
 
path, cost, expanded = astar('Hyd', 'Delhi')
print("A* Path :", " -> ".join(path))
print("Path Cost :", cost, "| Nodes Expanded :", expanded) 




