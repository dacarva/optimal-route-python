from collections import deque

adj = {0: [1, 3], 1: [2], 2: [1], 3: [4, 5],
       4: [3, 6, 7], 5: [3, 6], 6: [4, 7], 7: [4, 6]}

train_adj = {'A': ['B'], 'B': ['A', 'C'], 'C': ['B', 'D', 'G'], 'D': ['C', 'E'], 'E': [
    'D', 'F'], 'F': ['E', 'I'], 'G': ['C', 'H'], 'H': ['G', 'I'], 'I': ['H', 'F']}

express_stations = {'G': ['Green'], 'H': ['Red'], 'I': ['Green']}


def bfs(adj, s, express_train=None):
    if express_train:
        print('Express train', express_train)
    parent = {s: None}
    distances = {s: 0}

    queue = deque()
    queue.append(s)

    while queue:
        ref_station = queue.popleft()
        # print('Ref.', ref_station)

        for station in adj[ref_station]:
            # print('Current station =>', station)

            # Check of a neighbor station is express to recalculate

            if station not in distances:
                parent[station] = ref_station
                # print('parent', parent)
                # Si es un tren expreso no sumar distancia + 1

                if express_train == None or station not in express_stations:
                    distances[station] = distances[ref_station] + 1

                elif express_train not in express_stations[station]:
                    distances[station] = distances[ref_station] + 1
                else:
                    distances[station] = distances[ref_station]

                # distances[station] = distances[ref_station] + 1

                # print('Distances', distances)
                queue.append(station)

            elif distances[station] > distances[ref_station]:
                distances[station] = distances[ref_station] + 1
                parent[station] = ref_station

    return parent, distances


def get_path(node_a, node_b, adj):
    parent, distance = bfs(adj, node_a, 'Green')
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
