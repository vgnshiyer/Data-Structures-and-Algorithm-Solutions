def numBusesToDestination(routes: List[List[int]], source: int, target: int) -> int:
    if source == target: return 0

    buses_that_stop_here = defaultdict(list)
    for bus, route in enumerate(routes):
        for stop in route:
            # storing all the buses that stop here
            buses_that_stop_here[stop].append(bus)

    q = deque([source])
    buses_changed = 0 # we do a level order traversal
    taken = set()

    while q:
        # increment the number of buses_chaged
        buses_changed += 1

        num_stops = len(q)
        for _ in range(num_stops):
            stop = q.popleft()

            # exploring all the stops we can go from the current stop 
            # via all the buses that stop here
            for bus in buses_that_stop_here[stop]:
                # notice that we store our bus in visited array
                # as a bus can take us to multiple stops and we are 
                # avoiding revisiting all those stops
                if bus in taken: continue
                taken.add(bus)
                for next_stop in routes[bus]:
                    # If we reach our destination, we return the number of buses we changed to reach here
                    if next_stop == target: return buses_changed
                    # store the next stop in our queue
                    q.append(next_stop)
    
    return -1