# Uses python3
import sys


def dist(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5


def small_min_distance(points, start, end):
    result = sys.maxsize
    for i in range(start, end):
        for j in range(i + 1, end):
            result = min(result, dist(points[i], points[j]))
    return result


def min_dist_recur(points, start, end):
    if end - start <= 2:
        return small_min_distance(points, start, end)

    mid = start + (end - start) // 2

    d1 = min_dist_recur(points, start, mid)
    d2 = min_dist_recur(points, mid, end)

    d = min(d1, d2)
    mid_y = (points[mid][1] + points[mid - 1][1]) / 2

    smaller_d = []
    for i in range(start, end):
        if abs(points[i][1] - mid_y) < d:
            smaller_d.append(points[i])

    smaller_d = sorted(smaller_d, key=lambda a: a[0])
    length = len(smaller_d)
    for i in range(length):
        for j in range(i + 1, min(length, i + 8)):
            if abs(smaller_d[i][0] - smaller_d[j][0]) <= d:
                d_prime = dist(smaller_d[i], smaller_d[j])
                d = min(d_prime, d)
    return d


def minimum_distance(x, y, n):
    points = zip(x, y)
    y_sorted = sorted(points, key=lambda a: a[1])
    return min_dist_recur(y_sorted, 0, n)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    # print(x)
    # print(y)
    # x = [4, -2, -3, -1, 2, -4, 1, -1, 3, -4, -2]
    # y = [4, -2, -4, 3, 3, 0, 1, -1, -1, 2, 4]
    # n = 11
    print("{0:.9f}".format(minimum_distance(x, y, n)))
