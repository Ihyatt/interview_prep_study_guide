# Course Schedule ii

```python
def findOrder(tasks: int, prerequisites: List[List[int]]) -> List[int]:
    prereq_map = defaultdict(list)

    for courses in prerequisites:
        prereq_map[courses[1]].append(courses[0])
        prereq_map[courses[0]]

    sortedOrder = []
    visited_path = set()
    visited = set()
    def dfs(course):
        if course in visited_path: #visited_path is used to catch cycle in graph
            dfs.can_complete = False
            return
        visited_path.add(course)

        while prereq_map[course]:
            new_course = prereq_map[course].pop()
            dfs(new_course)
        visited_path.remove(course)
    
        if course not in visited:
            sortedOrder.append(course)
            visited.add(course)

    dfs.can_complete = True
    for course in range(0, tasks):
        dfs(course)
    
    sortedOrder.reverse()
    return sortedOrder if dfs.can_complete else []
```

```
Input: [ [ 2,5 ], [ 0,5 ], [ 0,4 ], [ 1,4 ], [ 3,2 ], [ 1,3 ] ]
Output: [ 1, 3, 2, 0 , 5, 4] #This is just one of the possible sorted answers
```

![Screen Shot 2021-08-30 at 6 58 54 PM](https://user-images.githubusercontent.com/11432315/131429969-d52540fb-5f29-44dd-b99c-fb99d0e1c044.png)

