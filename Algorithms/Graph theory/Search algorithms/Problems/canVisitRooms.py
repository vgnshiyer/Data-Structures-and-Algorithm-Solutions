class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [0] * n
        visited[0] = 1

        queue = deque([0])
        while queue:
            room = queue.popleft()
            for key in rooms[room]:
                if not visited[key]:
                    visited[key] = 1
                    queue.append(key)

        return all(visited) == 1