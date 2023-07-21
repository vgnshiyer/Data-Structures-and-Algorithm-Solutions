'''
Given an array of meeting time intervals consisting of start and end times[[s1,e1],[s2,e2],...](si< ei), determine if a person could attend all meetings.
Input:
[[0,30],[5,10],[15,20]]
Output:
 false
'''

# O(nlogn) Time O(1) Space
def canAttend(timings) -> bool:
    timings.sort()
    for i in range(1, len(timings)):
        if timings[i][0] < timings[i-1][1]: return False
    return True

print(canAttend([[0,30],[5,10],[15,20]])) # False
print(canAttend([[7,10],[2,4]])) # True