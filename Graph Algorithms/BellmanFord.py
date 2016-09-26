"""
Bellman-Ford algorithm
Time Complexity: O(EV)
"""

def shortestPath(graph, start):

    # Initialize distances.
    distance = {}
    for k in graph:
        distance[k] = float('inf')
    distance[start] = 0

    
    # Rellax all edges V -1 Times.
    for _ in range(len(graph)):
        for node in graph:
            for neighbour in graph[node]:
                if distance[neighbour] > (distance[node] + graph[node][neighbour]):
                    distance[neighbour] = (distance[node] + graph[node][neighbour])
    return distance

    # Check for negative-weight cycles.
    for node in graph:
        for neighbour in graph[node]:
            if distance[neighbour] > (distance[node] + graph[node][neighbour]):
                raise NameError('Negative weight cycle!')


if __name__ == "__main__":

    graph = {
        'A': { 'B': -1, 'C': 4 },
        'B': { 'C': 3, 'D': 2, 'E': 2 },
        'C': { },
        'D': { 'C': 5, 'B': 1 },
        'E': { 'D': -3 }
    }
    
    distance = shortestPath(graph,'A')
    for k in graph:
        print("Distance from [ A ] to [",k,"] -> ",distance[k])