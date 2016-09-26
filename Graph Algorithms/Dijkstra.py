'''
Dijkstra’s shortest path algorithm
Time Complexity: 
	* With Binary Heap     =   O(ELogV)
	* With Fibonacci Heap  =   O(E + VlogV)

Time Complexity Priority Queue: 
    * add       =   O(1) // We do not heapify
    * pop       =   O(log(n))
    * decrease  =   O(log(n))
'''

from PriorityQueue import PriorityQueue



def shortestPath(graph, start):

	visited = set()
	shortestDistance = dict()
	queue = PriorityQueue()
	
	# Add all the nodes inside the BHeap with priority -INF
	for n in graph:
		queue.add(float('inf'),n)

	# Decreas start point with Priority 0, and Heapify
	queue.decrease(start,0)

	while not queue.empty():

		distance, node = queue.pop()
		shortestDistance[node] = distance

		if node not in visited:
			visited.add(node)

		for neighbor in graph[node]:
			if neighbor in visited:
				continue

			# If new Distance is shorter, update with the new distance and heapify
			neighborDistance = queue.getPriority(neighbor)
			if neighborDistance > (distance + graph[node][neighbor]):
				queue.decrease(neighbor,(distance + graph[node][neighbor]))

	return shortestDistance



if __name__ == "__main__":

    graph = {
        '0': { '1': 4, '7': 8 },
        '1': { '2': 8, '7': 11, '0': 4 },
        '2': { '1': 8, '3': 7, '8': 2, '5': 4 },
        '3': { '2': 7, '4': 9, '5': 14 },
        '4': { '3': 9, '5': 10 },
        '5': { '3': 14, '4': 10, '2': 4, '6': 2 },
        '6': { '5': 2, '7': 1, '8': 6 },
        '7': { '0': 8, '1': 11, '6': 1, '8': 7 },
        '8': { '2': 2, '6': 6, '7': 7 }
    }
    
    distance = shortestPath(graph,'0')
    for k in graph:
        print("Distance from [ 0 ] to [",k,"] -> ",distance[k])