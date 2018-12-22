# Uses python3
import re
import sys


def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def min_max(i, j, ops, M, m):
    min_val = sys.maxsize
    max_val = -sys.maxsize
    for k in range(i, j):
        a = evalt(M[i][k], M[k + 1][j], ops[k])
        b = evalt(M[i][k], m[k + 1][j], ops[k])
        c = evalt(m[i][k], M[k + 1][j], ops[k])
        d = evalt(m[i][k], m[k + 1][j], ops[k])
        min_val = min(min_val, a, b, c, d)
        max_val = max(max_val, a, b, c, d)
    return min_val, max_val


def get_maximum_value(dataset):
    digits = list(map(lambda x: int(x), re.compile(r'[*+-]').split(dataset)))
    ops = list(filter(lambda x: x != '', re.compile(r'[0-9]').split(dataset)))
    n = len(digits)

    M = [[0 for i in range(n)] for j in range(n)]
    m = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        M[i][i] = digits[i]
        m[i][i] = digits[i]

    for s in range(1, n):
        for i in range(n - s):
            j = i + s
            min_val, max_val = min_max(i, j, ops, M, m)
            M[i][j] = max_val
            m[i][j] = min_val
    return M[0][n - 1]


if __name__ == "__main__":
    # str = "5-8+7*4-8+9"
    str = input()
    print(get_maximum_value(str))
