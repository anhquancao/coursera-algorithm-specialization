# Uses python3

import sys


def edit_distance(s, t):
    m = len(s) + 1
    n = len(t) + 1
    D = [[0] * n for i in range(m)]

    for i in range(1, m):
        for j in range(1, n):
            if s[i - 1] == t[j - 1]:
                D[i][j] = D[i - 1][j - 1] + 1
            else:
                D[i][j] = max(D[i - 1][j], D[i][j - 1], D[i - 1][j - 1])

    return D[m - 1][n - 1]


def lcs2(a, b):
    return edit_distance(a, b)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    # a = [2, 7, 8, 3]
    # b = [5, 2, 8, 7]
    print(lcs2(a, b))
