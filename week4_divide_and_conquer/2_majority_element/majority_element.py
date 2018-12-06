# Uses python3
import sys


def get_majority_element(a, left, right):
    count = 1
    current = left
    for i in range(left + 1, right):
        if a[current] == a[i]:
            count += 1
        else:
            count -= 1
        if count == 0:
            current = i
            count = 1

    count = 0
    for i in range(left, right):
        if a[i] == a[current]:
            count += 1
    if count > ((right - left) / 2):
        return 1
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
