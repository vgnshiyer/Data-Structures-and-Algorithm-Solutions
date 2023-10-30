'''
Sort elements according to their frequencies
'''

def bucket_sort(arr):
    temp = []

    counter = {}
    for n in arr:
        counter[n] = counter.get(n, 0) + 1

    for k, v in counter.items():
        temp.append((v, k))

    heapq.heapify(temp)

    order = []
    while temp:
        order.append(heapq.heappop(temp)[1])

    return order