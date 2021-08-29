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

