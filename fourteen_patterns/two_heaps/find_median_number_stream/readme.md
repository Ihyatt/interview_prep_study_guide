# Find the Median of a Number Stream


```python
class MedianOfAStream:
  def __init__(self):
    self.max_heap = []
    self.min_heap = []

    heapq.heapify(self.max_heap)
    heapq.heapify(self.min_heap)

  def insert_num(self, num):
    heapq.heappush(self.max_heap, -num)

    heapq.heappush(self.min_heap, -self.max_heap[0])
    heapq.heappop(self.max_heap)

    if len(self.min_heap) > len(self.max_heap):
      heapq.heappush(self.max_heap, -self.min_heap[0])
      heapq.heappop(self.min_heap)

  def find_median(self):
    if len(self.max_heap) == len(self.min_heap):
        return (-self.max_heap[0] + self.min_heap[0]) / 2
    else:
        return -self.max_heap[0]
```
