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



![Screen Shot 2021-09-02 at 6 32 57 PM](https://user-images.githubusercontent.com/11432315/131938241-21b56c90-2ba1-4a6a-a54b-8ceffb8f89ec.png)


```
medianOfAStream = MedianOfAStream()
medianOfAStream.insert_num(10)
```


![Screen Shot 2021-09-02 at 6 36 01 PM](https://user-images.githubusercontent.com/11432315/131938290-0e431c0a-786c-4fea-8dd0-dd3645be842f.png)


![Screen Shot 2021-09-02 at 6 36 31 PM](https://user-images.githubusercontent.com/11432315/131938315-211190ba-a932-4c48-8891-61bc9606496c.png)

```
medianOfAStream.insert_num(9)
medianOfAStream.find_median() --> 9.5
Each MIN and MAX heap must have at least one NODE. The LENGTH on MIN Heap should never be longer than LENGTH of MAX heap.
```


![Screen Shot 2021-09-02 at 6 41 09 PM](https://user-images.githubusercontent.com/11432315/131938358-792e72fb-2c32-48b4-bfcb-fa663cf5cafa.png)


```
medianOfAStream.insert_num(3)
medianOfAStream.insert_num(2)
medianOfAStream.insert_num(8)
medianOfAStream.insert_num(7)
medianOfAStream.find_median() --> 7.5
```


![Screen Shot 2021-09-02 at 6 43 50 PM](https://user-images.githubusercontent.com/11432315/131938409-a02882e2-0358-41ec-868d-d71e664b7b7f.png)

```
medianOfAStream.insert_num(7)
medianOfAStream.insert_num(1)
medianOfAStream.find_median() --> 7.0

```
