def heapsort(unsorted_list): # changing the argument to unsorted_list to match more with python vanacular
    # create an empty heap to hold the sorted max heap
    sorted_max_heap = Heap()

    # loop over the unsorted list and insert each element in to the sorted max heap
    for elem in unsorted_list:
        sorted_max_heap.insert(elem)

    # created an empty list to hold the sorted list data
    sorted_list = []
    
    # while the sorted max heaps storage has values append the values to the sorted list
    # by way of the heaps delete method
    while len(sorted_max_heap.storage) > 0:
        sorted_list.append(sorted_max_heap.delete())
    
    # reverse the sorted_list to ascending order to make it min sorted
    sorted_list.reverse()

    # return the sorted list to the caller
    return sorted_list
class Heap:
  def __init__(self):
    self.storage = []
    
  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1)

  def delete(self):
    retval = self.storage[0]
    self.storage[0] = self.storage[len(self.storage) - 1]
    self.storage.pop()
    self._sift_down(0)
    return retval 

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    while (index - 1) // 2 >= 0:
      if self.storage[(index - 1) // 2] < self.storage[index]:
        self.storage[index], self.storage[(index - 1) // 2] = self.storage[(index - 1) // 2], self.storage[index]
      index = (index - 1) // 2

  def _sift_down(self, index):
    while index * 2 + 1 <= len(self.storage) - 1:
      mc = self._max_child(index)
      if self.storage[index] < self.storage[mc]:
        self.storage[index], self.storage[mc] = self.storage[mc], self.storage[index]
      index = mc

  def _max_child(self, index):
    if index * 2 + 2 > len(self.storage) - 1:
      return index * 2 + 1
    else:
      return index * 2 + 1 if self.storage[index * 2 + 1] > self.storage[index * 2 + 2] else index * 2 + 2