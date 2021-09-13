class MinHeap:

    def __init__(self, array):
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        firstParentIndex = (len(array) - 2)//2
        for currentIndex in reversed(range(firstParentIndex+1)):
            self.siftDown(currentIndex, len(array)-1, array)
        return array

    def siftDown(self, currentIndex, endIndex, heap):
        childOneIndex = currentIndex*2 + 1

        while childOneIndex <= endIndex:
            childTwoIndex = currentIndex*2 + 2 if currentIndex*2 + 2 <= endIndex else -1

            if childTwoIndex != -1 and heap[childTwoIndex] < heap[childOneIndex]:
                indexToSwap = childTwoIndex
            else:
                indexToSwap = childOneIndex
            if heap[currentIndex] > heap[indexToSwap]:
                self.swap(currentIndex, indexToSwap, heap)
                currentIndex = indexToSwap
                childOneIndex = currentIndex*2 + 1
            else:
                return

    def siftUp(self, currentIndex, heap):
        parentIndex = (currentIndex-1)//2

        while parentIndex > 0 and heap[parentIndex] > heap[currentIndex]:
            self.swap(parentIndex, currentIndex, heap)
            currentIndex = parentIndex
            parentIndex = (currentIndex - 1)//2

    def peek(self):
        return self.heap[0]

    def insert(self, element):
        self.heap.append(element)
        self.siftUp(len(self.heap)-1, self.heap)

    def remove(self):
        self.swap(0, len(self.heap)-1, self.heap)
        valuetoRemove = self.heap.pop()
        self.siftDown(0, len(self.heap)-1, self.heap)
        return valuetoRemove

    def swap(self, index1, index2, heap):
        heap[index1], heap[index2] = heap[index2], heap[index1]


mHeap = MinHeap([1, 3, 4, 2, 5, 6, 3, 2])

print(mHeap.peek())
