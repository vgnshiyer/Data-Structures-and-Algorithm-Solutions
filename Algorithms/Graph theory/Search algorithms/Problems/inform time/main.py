class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        heirarchy = defaultdict(list)
        for i in range(n):
            if manager[i] == -1: continue
            heirarchy[manager[i]].append(i)

        def inform(emp):
            inform_time = 0
            for sub in heirarchy[emp]:
                inform_time = max(inform_time, inform(sub))
            return inform_time + informTime[emp]

        return inform(headID)