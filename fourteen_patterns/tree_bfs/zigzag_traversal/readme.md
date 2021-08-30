# Zigzag Traversal


```python
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
```

![Screen Shot 2021-08-30 at 10 41 55 AM](https://user-images.githubusercontent.com/11432315/131381548-6ce15e46-701c-4676-93bb-9296adb95810.png)

![Screen Shot 2021-08-30 at 12 35 27 PM](https://user-images.githubusercontent.com/11432315/131394947-d34d4e48-e0f1-4cd0-9130-57b3dc639b33.png)
