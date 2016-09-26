'''
Shortest Path in DAG Algorithm
Time Complexity: O(V+E)
'''
from TopologicalSort import topologicalSort

def shortestPath(graph, start):

    queue = topologicalSort(graph)
    distance = dict()
    for k in graph:
        distance[k] = float('inf')
    distance[start] = 0 # We add the starting node with 0

    while queue:
        node = queue.popleft()
        if distance[node] != float('inf'):
            for vertex in graph.get(node,()):
                if distance[vertex] > (distance[node] + graph[node][vertex]):
                    distance[vertex] = (distance[node] + graph[node][vertex])

    return distance


if __name__ == "__main__":

    graph = {
        't': { 'x': 7, 'z': 2, 'y': 4 },
        'x': { 'y': -1, 'z': 1 },
        'r': { 't': 3, 's': 5 },
        'y': { 'z': -2 },
        's': { 't': 2, 'x': 6 },
        'z': {}
    }

    distance = shortestPath(graph,'s')
    for k in graph:
        print("Distance from [ s ] to [",k,"] -> ",distance[k])
