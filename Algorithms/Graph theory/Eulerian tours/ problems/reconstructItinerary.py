
def findItinerary(tickets: List[List[str]]) -> List[str]:
    adj = defaultdict(list)
    
    for src, dest in sorted(tickets, reverse=True):
        adj[src].append(dest)

    itinerary = []
    def eulerianTour(src):
        while adj[src]:
            nxt = adj[src].pop()
            eulerianTour(nxt)
        itinerary.append(src)
    
    eulerianTour('JFK')
    return itinerary[::-1]
