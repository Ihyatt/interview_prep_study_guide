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
    