graph = {
    'a': {'b': 2, 'd': 4},
    'b': {'a': 2, 'c': 3},
    'c': {'b': 3, 'd': 1},
    'd': {'a': 4, 'c': 1}
}

total_cost = 0
print("edge_costs:")
for vertex, edges in graph.items():
    for neighbour, cost in edges.items():
        print(f"cost from {vertex} to {neighbour}:{cost}")
        total_cost += cost
total_cost //= 2
print(f"\ntotal cost of edges: {total_cost}")



