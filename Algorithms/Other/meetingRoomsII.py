'''
Given an array of meeting time intervals consisting of start and end times[[s1,e1],[s2,e2],...](si< ei), find the minimum number of conference rooms required.
Input:
[[0, 30],[5, 10],[15, 20]]
Output:
 2
'''

import heapq

# O(n^2) Time O(1) Space
def meetingRooms(timings):
    timings.sort()
    rooms = [0]*len(timings)

    for s, e in timings:
        for i, r in enumerate(rooms):
            if r < e: 
                rooms[i] = e # assign room
                break
    return rooms.index(0)

# O(nlogn) Time, O(n) Space -> Priority Queue
def meetingRooms2(timings):
    timings.sort() # O(nlogn)
    rooms = [] # min-heap

    for s, e in timings:
        if rooms and rooms[0] < s: heapq.heappop(rooms)
        heapq.heappush(rooms, e)
    return len(rooms)

# O(nlogn) Time O(n) Space -> Two pointers
def meetingRooms3(timings):
    start, end = [], []
    for s, e in timings:
        start.append(s)
        end.append(e)
    
    start.sort()
    end.sort()

    p1 = p2 = usedRooms = 0
    while p1 < len(timings):
        # check if a meeting has ended
        if start[p1] >= end[p2]:
            usedRooms -= 1 # free up a room
            p2 += 1 # assign new end time
        
        usedRooms += 1 # assign a room
        p1 += 1 # go to assign next meeting
    return usedRooms

print(meetingRooms3([[0, 30],[5, 10],[15, 20]])) # 2
print(meetingRooms3([[7,10],[2,4]])) # 1