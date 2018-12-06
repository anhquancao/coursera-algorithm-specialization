# Uses python3
import sys


def bin_recur(a, left, right, x):
    mid = int((left + right) / 2)
    if left > right:
        return -1
    if a[mid] == x:
        return mid
    elif x > a[mid]:
        return bin_recur(a, mid + 1, right, x)
    else:
        return bin_recur(a, left, mid - 1, x)


def binary_search(a, x):
    left, right = 0, len(a) - 1
    # write your code here
    return bin_recur(a, left, right, x)


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1: n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end=' ')
