from typing import List

def findOrder(tasks: int, prerequisites: List[List[int]]) -> List[int]:
    prereq_map = defaultdict(list)

    for courses in prerequisites:
        prereq_map[courses[1]].append(courses[0])
        prereq_map[courses[0]]

    sortedOrder = []
    visited_path = set()
    visited = set()
    def dfs(course):
        if course in visited_path:
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