def find_dependencies(graph):
    result = {}
    for node, children in graph.items():
        if node not in result:
            result[node] = 0

        for child in children:
            if child not in result:
                result[child] = 1
            else:
                result[child] += 1
    return result


def independent_nodes(node_dependencies):
    for node, dependencies in node_dependencies.items():
        if dependencies == 0:
            return node
    return None


nodes = int(input())

graph = {}

for _ in range(nodes):
    line_parts = input().split('->')
    node = line_parts[0].strip()
    children = line_parts[1].strip().split(', ') if line_parts[1] else []
    graph[node] = children

node_dependencies = find_dependencies(graph)
has_loops = False
sorted_nodes = []

while node_dependencies:
    removal_nodes = independent_nodes(node_dependencies)
    if removal_nodes is None:
        has_loops = True
        break

    node_dependencies.pop(removal_nodes)
    sorted_nodes.append(removal_nodes)
    for child in graph[removal_nodes]:
        node_dependencies[child] -= 1

if has_loops:
    print("Invalid topological sorting")
else:
    print(f"Topological sorting: {', '.join(sorted_nodes)}")