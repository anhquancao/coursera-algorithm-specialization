# Uses python3
import sys
import itertools


def partition3(A, n):
    s = sum(A)
    if s % 3 != 0:
        return False
    subsum = int(s / 3)

    S = [[[0 for i in range(subsum + 1)] for j in range(subsum + 1)] for k in range(n + 1)]

    for s1 in range(1, subsum + 1):
        for s2 in range(1, subsum + 1):
            S[0][s1][s2] = False

    for i in range(n + 1):
        S[i][0][0] = True

    for i in range(1, n + 1):
        for s1 in range(subsum + 1):
            for s2 in range(subsum + 1):
                S[i][s1][s2] = S[i - 1][s1][s2]
                # a = S[i][s1][s2]
                e = A[i - 1]
                if s1 >= e:
                    # t1 = S[i - 1][s1 - e][s2]
                    # t2 = S[i][s1][s2]
                    S[i][s1][s2] = S[i][s1][s2] or S[i - 1][s1 - e][s2]
                if s2 >= e:
                    # t1 = S[i - 1][s1][s2 - e]
                    # t2 = S[i][s1][s2]
                    S[i][s1][s2] = S[i][s1][s2] or S[i - 1][s1][s2 - e]

    return S[n][subsum][subsum]


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    # n = 3
    # A = [2, 2, 2]
    if partition3(A, n):
        print(1)
    else:
        print(0)
