# Level Order Traversal


```python
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
```


![Screen Shot 2021-08-30 at 9 58 06 AM](https://user-images.githubusercontent.com/11432315/131376974-887a982c-4a93-4fa7-8e30-f3748caae6ed.png)



![Screen Shot 2021-08-30 at 10 37 41 AM](https://user-images.githubusercontent.com/11432315/131381112-e4e450e3-528e-4afe-8475-b098068c93a6.png)

```
Get length of queue with N, and iterate from 0 -> N to avoid iterating nodes not on current level
```
