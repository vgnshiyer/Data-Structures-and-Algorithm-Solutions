'''
Pay attention to the way the answer is sorted. 
'''
def watchedVideosByFriends(watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
    q = deque([id])
    visited = set([id])
    while q:
        if level == 0:
            videos = []
            for j in q:
                videos.extend(watchedVideos[j])
            counts = Counter(videos)
            return sorted(counts.keys(), key = lambda x: (counts[x], x))

        s = len(q)
        while s:
            s -= 1
            i = q.popleft()
            for j in friends[i]:
                if j not in visited:
                    visited.add(j)
                    q.append(j)
        
        level -= 1
    return []