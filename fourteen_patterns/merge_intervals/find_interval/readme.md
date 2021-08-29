# Interval Finding 

```python
from typing import List, Optional


def merge(intervals_a: List[Optional[List[int]]], intervals_b: List[Optional[List[int]]]) -> List[Optional[List[int]]]:
  result = []
  p_a, p_b = 0, 0
  while p_a < len(intervals_a) and p_b < len(intervals_b):
    is_intersection = max(intervals_a[p_a][0] , intervals_b[p_b][0]) <= min(intervals_a[p_a][1] , intervals_b[p_b][1])
    if is_intersection:
      result.append([max(intervals_a[p_a][0] , intervals_b[p_b][0]), min(intervals_a[p_a][1] , intervals_b[p_b][1])])
    if intervals_a[p_a][1] < intervals_b[p_b][1]:
      p_a += 1
    else:
      p_b += 1
  return result
```

![interval1](https://user-images.githubusercontent.com/11432315/131265730-0cee5b28-0288-419d-b07e-bc253823351e.png)
```
Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
```

```
[[0,2],[5,10],[13,23],[24,25]]
   *

[[1,5],[8,12],[15,24],[25,26]]
   *

result = [[1,2]]

To find if an intersection exists, get the MAX of firstList[*][0] and secondList[*][0] and MIN of firstList[*][1] and secondList[*][1]
If MAX of 0th item is less than or equal to MIN of 1st item, then an intersection has been found
```


```
[[0,2],[5,10],[13,23],[24,25]]
          *

[[1,5],[8,12],[15,24],[25,26]]
   *

result = [[1,2], [5,5]]
Move pointer for the array where the item at 1st index is the less value.
```
