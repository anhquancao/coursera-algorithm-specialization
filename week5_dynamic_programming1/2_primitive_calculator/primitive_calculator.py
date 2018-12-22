# Uses python3
import sys


def compute_min_ops(n):
    res = [0] * (n + 1)
    for i in range(1, n + 1):
        min1 = res[i - 1] + 1
        min2 = sys.maxsize
        min3 = sys.maxsize
        if i % 3 == 0:
            min2 = res[i // 3] + 1
        if i % 2 == 0:
            min3 = res[i // 2] + 1
        res[i] = min(min1, min2, min3)
    return res


def backtrack(n, min_ops, seq):
    if n == 0:
        return seq
    min1 = min_ops[n - 1]
    min2 = sys.maxsize
    min3 = sys.maxsize
    if n % 3 == 0:
        min2 = min_ops[n // 3]
    if n % 2 == 0:
        min3 = min_ops[n // 2]
    min_op = min(min1, min2, min3)
    if min1 == min_op:
        return backtrack(n - 1, min_ops, seq + [n])
    if min2 == min_op:
        return backtrack(n // 3, min_ops, seq + [n])
    if min3 == min_op:
        return backtrack(n // 2, min_ops, seq + [n])


def optimal_sequence(n):
    min_ops = compute_min_ops(n)
    return list(reversed(backtrack(n, min_ops, [])))



input = sys.stdin.read()
n = int(input)
sequence = optimal_sequence(n)
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
