from collections import deque

adj = {0: [1, 3], 1: [2], 2: [1], 3: [4, 5],
       4: [3, 6, 7], 5: [3, 6], 6: [4, 7], 7: [4, 6]}

train_adj = {'A': ['B'], 'B': ['A', 'C'], 'C': ['B', 'C', 'G'], 'D': ['C', 'E'], 'E': [
    'D', 'F'], 'F': ['E', 'I'], 'G': ['C', 'H'], 'H': ['G', 'I'], 'I': ['H', 'F']}


def bfs(adj, s):
    parent = {s: None}
    d = {s: 0}

    queue = deque()
    queue.append(s)

    while queue:
        u = queue.popleft()

        for n in adj[u]:
            if n not in d:
                parent[n] = u
                d[n] = d[u] + 1
                queue.append(n)

    return parent, d


def get_path(node_a, node_b, adj):
    parent, distance = bfs(adj, node_a)
    print('parent', parent)
    print('distance', distance)

    node = node_b
    path = [node]

    while distance[node] > 0:
        node = parent[node]
        path.append(node)
    return path


node_a = 'A'
node_b = 'F'
print('Path', get_path(node_a, node_b, train_adj))
