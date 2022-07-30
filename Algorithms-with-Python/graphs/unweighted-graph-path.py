from collections import deque

nodes = int(input())
edges = int(input())

graph = []

[graph.append([]) for _ in range(nodes + 1)]

for _ in range(edges):
    source, destination = [int(x) for x in input().split()]
    graph[source].append(destination)

start_node = int(input())
destination_node = int(input())

visited = [False] * (nodes + 1)
parent = [None] * (nodes + 1)

visited[start_node] = True
queue = deque([start_node])

while queue:
    node = queue.popleft()
    if node == destination_node:
        break
    for child in graph[node]:
        if visited[child]:
            continue
        visited[child] = True
        queue.append(child)
        parent[child] = node

shortest_path = deque()
node = destination_node
while node is not None:
    shortest_path.appendleft(node)
    node = parent[node]

print(len(shortest_path) - 1)  # length of the shortest path
print(*shortest_path)  # path of nodes

