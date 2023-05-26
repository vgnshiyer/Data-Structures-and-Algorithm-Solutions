def hanoi(n, a, b, c):
    if n <= 0: return
    if n == 1:
        print(a, c)
        return

    hanoi(n-1, a, c, b)
    print(a, c)
    hanoi(n-1, b, a, c)

if __name__ == '__main__':
    hanoi(3, 1,2,3)