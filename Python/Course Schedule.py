from typing import List
from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = defaultdict(int)
        for i in range(numCourses):
            in_degree[i] = 0
        children = defaultdict(list)
        for p in prerequisites:
            in_degree[p[0]] += 1
            children[p[1]].append(p[0])
        queue = []
        for course, degree in in_degree.items():
            if degree == 0:
                queue.append(course)
        done = 0
        while len(queue) > 0:
            course = queue.pop()
            done += 1
            for child in children[course]:
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    queue.append(child)
        return done == numCourses
