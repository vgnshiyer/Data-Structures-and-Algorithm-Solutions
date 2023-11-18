'''
The examples in the problem description are deluding. I first tried to solve it with topological sorting by including some greedy method with a heap. But it seems like there is no way to figure out the most optimal solution unless you explore all possibilities. This gives way for dynamic programming appraoch which should have been apparent looking at the constraints for the problem. 

With this, it is translated into a travelling salesman problem, where we need to find the minimum number of semesters to complete all courses. (With a slight variation of at most k courses each semester)

Another difference is, we are taking multiple courses in one recursive call, unline just 1 selected in normal TSP implementation. --> To tackle this, we use combinations (n Choose k)
'''
def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
    indegree = [0] * n
    adj = defaultdict(list)

    for i, j in relations:
        indegree[j - 1] += 1
        adj[i - 1].append(j - 1)

    @cache
    def dfs(mask, indegree):
        # all courses taken - u are graduated
        if mask == (1 << n) - 1: return 0

        ans = inf
        # can take all courses which have not yet been taken and have no prereqs left
        can_take = [i for i in range(n) if indegree[i] == 0 and not mask & (1 << i)]
        # recurse on all possible combination of min(n, k) courses
        for courses in combinations(can_take, min(k, len(can_take))):
            new_mask, new_indegree = mask, list(indegree)

            for course in courses:
                # mark course as taken
                new_mask |= (1 << course)
                
                # since a parent course is taken, reduce prereq for all associated child courses
                for next_course in adj[course]:
                    new_indegree[next_course] -= 1
            # add a semester 
            ans = min(ans, 1 + dfs(new_mask, tuple(new_indegree)))
        return ans

    return dfs(0, tuple(indegree))