class MinPriorityQueue:
    def __init__(self):
        """
        Initialize an empty MinPriorityQueue using a binary heap.
        """
        self.heap = []  # This will store the heap elements as (key, node)
        self.position_map = {}  # This helps to find the index of nodes in the heap quickly for decrease_key operation

    def _parent(self, index):
        return (index - 1) // 2

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _swap(self, i, j):
        """
        Swap two elements in the heap and update their positions in the position_map.
        """
        self.position_map[self.heap[i][1]], self.position_map[self.heap[j][1]] = j, i
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _heapify_up(self, index):
        """
        Move the element at the given index up to its proper position in the heap.
        """
        parent_index = self._parent(index)
        while index > 0 and self.heap[index][0] < self.heap[parent_index][0]:
            self._swap(index, parent_index)
            index = parent_index
            parent_index = self._parent(index)

    def _heapify_down(self, index):
        """
        Move the element at the given index down to its proper position in the heap.
        """
        smallest = index
        left = self._left_child(index)
        right = self._right_child(index)

        if left < len(self.heap) and self.heap[left][0] < self.heap[smallest][0]:
            smallest = left

        if right < len(self.heap) and self.heap[right][0] < self.heap[smallest][0]:
            smallest = right

        if smallest != index:
            self._swap(index, smallest)
            self._heapify_down(smallest)

    def insert(self, key, node):
        """
        Insert a new element (key, node) into the priority queue.
        
        :param key: The key value (d'(u)) to order by.
        :param node: The node (u) associated with the key.
        """
        self.heap.append((key, node))
        index = len(self.heap) - 1
        self.position_map[node] = index
        self._heapify_up(index)

    def extract_min(self):
        """
        Extract the element with the minimum key (d'(u)) from the priority queue.
        
        :return: The (key, node) pair with the smallest key.
        """
        if len(self.heap) == 0:
            raise IndexError("extract_min from an empty priority queue")

        root = self.heap[0]
        last_element = self.heap.pop()
        
        if len(self.heap) > 0:
            self.heap[0] = last_element
            self.position_map[last_element[1]] = 0
            self._heapify_down(0)

        del self.position_map[root[1]]
        return root

    def decrease_key(self, node, new_key):
        """
        Decrease the key of a given node in the priority queue.
        
        :param node: The node (u) whose key (d'(u)) should be decreased.
        :param new_key: The new key value (d'(u)) to update.
        """
        index = self.position_map[node]
        current_key, _ = self.heap[index]

        if new_key > current_key:
            raise ValueError("new key is greater than current key")

        self.heap[index] = (new_key, node)
        self._heapify_up(index)

    def is_empty(self):
        """
        Check if the priority queue is empty.
        
        :return: True if the priority queue is empty, False otherwise.
        """
        return len(self.heap) == 0

# Example usage:
pq = MinPriorityQueue()
pq.insert(10, 'a')
pq.insert(5, 'b')
pq.insert(20, 'c')

print(pq.extract_min())  # Output: (5, 'b')
pq.decrease_key('c', 1)
print(pq.extract_min())  # Output: (1, 'c')
print(pq.extract_min())  # Output: (10, 'a')
