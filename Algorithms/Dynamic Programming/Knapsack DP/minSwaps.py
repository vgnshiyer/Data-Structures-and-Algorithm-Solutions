def minSwap(self, A, B):
    '''
    swap[i] = min swaps to make A[0:i] and B[0:i] increasing, if we swap A[i] and B[i]
    not_swap[i] = min swaps to make A[0:i] and B[0:i] increasing, if we do not swap A[i] and B[i]

    1) if n1[i-1] < n1[i] and n2[i-1] < n2[i]
        We have two options:
            a) do not swap n1[i] and n2[i] and n1[i-1] and n2[i-1].
                not_swap[i] = not_swap[i-1]
            b) swap both n1[i] and n2[i] and n1[i-1] and n2[i-1].
                swap[i] = swap[i-1] + 1
    2) if n1[i-1] < n2[i] and n2[i-1] < n1[i]
        We have two options:
            a) swap n1[i-1] and n2[i-1] and don't swap n1[i] and n2[i].
                not_swap[i] = min(swap[i-1], not_swap[i])
            b) swap n1[i] and n2[i] and don't swap n1[i-1] and n2[i-1].
                swap[i] = min(swap[i], not_swap[i-1] + 1)
    '''
    N = len(A)
    not_swap, swap = [N] * N, [N] * N
    not_swap[0], swap[0] = 0, 1
    for i in range(1, N):
        if A[i - 1] < A[i] and B[i - 1] < B[i]:
            swap[i] = swap[i - 1] + 1
            not_swap[i] = not_swap[i - 1]
        if A[i - 1] < B[i] and B[i - 1] < A[i]:
            swap[i] = min(swap[i], not_swap[i - 1] + 1)
            not_swap[i] = min(not_swap[i], swap[i - 1])
    return min(swap[-1], not_swap[-1])