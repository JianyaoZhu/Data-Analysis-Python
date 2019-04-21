nodes = ('1', '2', '3', '4', '5', '6')
graph = {
    '1': {'2': 2, '3': 8},
    '2': {'3': 5, '4': 3},
    '3': {'2': 6, '5': 0},
    '4': {'3': 1, '5': 7, '6': 6},
    '5': {'4': 4},
    '6': {'5': 2}}

unvisited = {node: None for node in nodes}
visited_node = {}
current = '1'
currentDistance = 0
unvisited[current] = currentDistance

while True:
    for neighbour, distance in graph[current].items():
        if neighbour not in unvisited:
            continue
        newDistance = currentDistance + distance
        if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
            unvisited[neighbour] = newDistance
    visited_node[current] = currentDistance
    del unvisited[current]
    if not unvisited:
        break
    candidates = [node for node in unvisited.items() if node[1]]
    current, currentDistance = sorted(candidates, key=lambda x: x[1])[0]

print(visited_node)
print('The shortest path is:', currentDistance)
