from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_degree = {}
        for i in range(numCourses):
            in_degree[i] = 0
        children = {}
        for p in prerequisites:
            in_degree[p[0]] = in_degree.get(p[0], 0) + 1
            children[p[1]] = children.get(p[1], []) + [p[0]]
        queue = []
        for course, degree in in_degree.items():
            if degree == 0:
                queue.append(course)
        res = []
        while len(queue) > 0:
            course = queue.pop()
            res.append(course)
            for child in children.get(course, []):
                in_degree[child] = in_degree.get(child) - 1
                if in_degree[child] == 0:
                    queue.append(child)
        return res if len(res) == numCourses else []