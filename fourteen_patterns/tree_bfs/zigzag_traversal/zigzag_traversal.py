from typing import List
from collections import deque

def zig_zag(root: TreeNode) -> List[List[int]]:
    ans = []
    if not root:
        return ans
    
    q = deque()
    
    q.append(root)
    reverse = False
    while q:
        n = len(q)
        level = []
        for i in range(n):
            if reverse: 
                node = q.pop()
                if node.right:
                    q.appendleft(node.right)
                if node.left:
                    q.appendleft(node.left)
                level.append(node.val)
            else:
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                level.append(node.val)
        ans.append(level)
        reverse = not reverse
    return ans
            