class Solution:
    def waysToBuildRooms(self, prevRoom: List[int]) -> int:
        mod = 10 ** 9 + 7
        adj = defaultdict(list)
        for i in range(len(prevRoom)):
            if prevRoom[i] == -1: continue
            adj[prevRoom[i]].append(i)

        def find_num_ways(room, prev_room = -1):
            # number of ways to arrange dependant rooms at this room
            dpi = 1

            # collect all num of dependant rooms
            num_rooms = []
            total = 0
            for next_room in adj[room]:
                if next_room == prev_room: continue
                # resolve all dependant rooms
                dpj, n_next_room = find_num_ways(next_room, room)
                dpi *= dpj
                dpi %= mod

                # collect num of rooms
                num_rooms.append(n_next_room)
                total += n_next_room

            # arrange dependant rooms at room
            n = total
            while n and num_rooms:
                r = num_rooms.pop()
                dpi *= comb(n, r)
                dpi %= mod
                n -= r

            # total ways to arrange dependant rooms, total rooms
            return dpi, total + 1

        return find_num_ways(0)[0]