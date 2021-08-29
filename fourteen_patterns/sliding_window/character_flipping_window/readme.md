# Character Flipping Window


```python
from typing import List


def longestOnes(nums: List[int], k: int) -> int:
    flips = 0 
    max_count = count = 0 
    l = 0

    for r in range(len(nums)):
        if nums[r] == 0:
            flips += 1
            count += 1
            while flips > k:
                if nums[l] == 0:
                    flips -= 1
                count -= 1
                l += 1     
        if nums[r] == 1:
            count += 1
        
            
        max_count = max(max_count, count)

    return max_count
```    


```
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
```


```
[0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
 L
 R
 
 count = 1 
 max_count = 1 
 flips = 1 
 
 Initialize LEFT and RIGHT pointer at 0. 
 If nums at RIGHT pointer is equal to 0, increase flips, increase count
 ```
 
 
 ```
[0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
 L
           R
 
 count = 6
 max_count = 5
 flips = 4
 
 If flips is greater than k, move LEFT pointer until flips is equal to k.
 Decrement count and flips as you move left.
```


```
[0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
     L 
                       R
 
 count = 10
 max_count = 10
 flips = 3
 
 Use MAX_COUNT to keep track of greatest COUNT so far. 
 ```
