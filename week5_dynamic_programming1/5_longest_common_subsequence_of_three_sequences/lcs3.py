# Uses python3

import sys


def edit_distance(a, b, c):
    an = len(a)
    bn = len(b)
    cn = len(c)
    D = [[[0] * (an + 1) for j in range(bn + 1)] for i in range(cn + 1)]

    for i in range(1, cn + 1):
        for j in range(1, bn + 1):
            for k in range(1, an + 1):
                # print(i, j, k)
                if c[i - 1] == b[j - 1] == a[k - 1]:
                    D[i][j][k] = D[i - 1][j - 1][k - 1] + 1
                else:
                    D[i][j][k] = max(D[i - 1][j][k], D[i][j - 1][k], D[i][j][k - 1],
                                  D[i - 1][j - 1][k], D[i - 1][j][k - 1], D[i][j - 1][k - 1],
                                  D[i - 1][j - 1][k - 1])

    return D[cn][bn][an]


def lcs3(a, b, c):
    # write your code here
    return edit_distance(a, b, c)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    # a = [1, 2, 3]
    # b = [2, 1, 3]
    # c = [1, 3, 5]
    print(lcs3(a, b, c))
