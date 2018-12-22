# Uses python3
def edit_distance(s, t):
    m = len(s) + 1
    n = len(t) + 1
    D = [[0]*n for i in range(m)]

    for i in range(m):
        D[i][0] = i

    for j in range(n):
        D[0][j] = j

    for i in range(1, m):
        for j in range(1, n):
            insertion = D[i - 1][j] + 1
            deletion = D[i][j - 1] + 1
            match = D[i - 1][j - 1]
            mismatch = D[i - 1][j - 1] + 1

            if s[i - 1] == t[j - 1]:
                D[i][j] = min(insertion, deletion, match)
            else:
                D[i][j] = min(insertion, deletion, mismatch)

    return D[m - 1][n - 1]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
    # print(edit_distance('short', 'ports'))
