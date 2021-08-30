from typing import List
from collections import deque


def binary_tree_level_order_traversal(node:TreeNode) -> List[List[int]]:
    q = deque()
    ans = []
    if not node:
        return ans
    q.append(node)
    while q:
        temp = []
        n = len(q)
        for i in range(n):
            node = q.popleft()
            temp.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        ans.append(temp)
        
    return ans