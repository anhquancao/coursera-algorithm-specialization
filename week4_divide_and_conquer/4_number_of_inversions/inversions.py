# Uses python3
import sys


def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    # write your code here
    min = left
    oldLeft = left
    oldAve = ave
    while left < oldAve and ave < right:
        xLeft = a[left]
        xRight = a[ave]
        if a[left] <= a[ave]:
            b[min] = a[left]
            left += 1
        elif a[left] > a[ave]:
            number_of_inversions += (oldAve - left)
            b[min] = a[ave]
            ave += 1
        min += 1

    # remains = 0
    while left < oldAve:
        # remains += 1
        b[min] = a[left]
        min += 1
        left += 1
    # if remains > 0:
    #     number_of_inversions += (remains - 1) * (right - oldAve)

    while ave < right:
        b[min] = a[ave]
        min += 1
        ave += 1

    for i in range(oldLeft, right):
        a[i] = b[i]

    return number_of_inversions


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    # n, a = 6, [9, 8, 7, 3, 2, 1]
    # n, a = 5, [2, 3, 9, 2, 9]
    # n, a = 5, [7, 8, 4, 5, 6]
    # n, a = 6, [3, 4, 6, 1, 2, 5]
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)))
    # print(b)
