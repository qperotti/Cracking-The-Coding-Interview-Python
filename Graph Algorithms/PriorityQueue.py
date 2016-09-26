'''
Priority Queue for Dijkstra Algorithm

Time Complexity: 
    * add       =   O(1) // We do not heapify
    * pop       =   O(log(n))
    * decrease  =   O(log(n))
'''

class PriorityQueue:

    def __init__(self):
        self.nodes = []
        self.total_nodes = 0
        self.indexs = {}

    
    def add(self, priority, node):

        self.nodes.append((priority,node))
        self.indexs[node] = self.total_nodes
        self.total_nodes += 1
    


    def pop(self):

        def popHeapify(index):
            left = (index * 2) + 1
            right = (index * 2) + 2
            min_val = index

            if left < self.total_nodes and self.nodes[left] < self.nodes[min_val]:
                min_val = left
            if right < self.total_nodes and self.nodes[right] < self.nodes[min_val]:
                min_val = right

            if min_val != index:
                minIndex, currentIndex = self.nodes[min_val][1], self.nodes[index][1]
                self.indexs[minIndex], self.indexs[currentIndex ] = self.indexs[currentIndex], self.indexs[minIndex]
                self.nodes[min_val], self.nodes[index] = self.nodes[index], self.nodes[min_val]
                popHeapify(min_val)


        if self.empty():
            return

        node = self.nodes[0]
        firstIndex, lastIndex = self.nodes[0][1], self.nodes[self.total_nodes-1][1]
        self.indexs[lastIndex] = self.indexs[firstIndex]
        self.nodes[0], self.nodes[self.total_nodes-1] = self.nodes[self.total_nodes-1], self.nodes[0]
        self.nodes.pop()
        del self.indexs[firstIndex]

        self.total_nodes -= 1
        popHeapify(0)
        
        return node

    def decrease(self, node, priority):

        def decreaseHeapify(index):
            if self.nodes[index//2] > self.nodes[index]:
                parentIndex, childIndex = self.nodes[index//2][1], self.nodes[index][1]
                self.indexs[parentIndex], self.indexs[childIndex ] = self.indexs[childIndex], self.indexs[parentIndex]
                self.nodes[index//2], self.nodes[index] = self.nodes[index], self.nodes[index//2]
                decreaseHeapify(index//2)

        index = self.indexs[node]
        self.nodes[index] = (priority,node)
        decreaseHeapify(index)


    def empty(self):
        return self.total_nodes < 1

    def getPriority(self,node):
        return self.nodes[self.indexs.get(node)][0]

    


