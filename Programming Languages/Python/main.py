## sort a list of tuples with the rightmost value
arr = [(1,5), (5,4), (1,3)]
arr.sort(key = lambda i : i[1])
print(arr) # [(1, 3), (5, 4), (1, 5)]