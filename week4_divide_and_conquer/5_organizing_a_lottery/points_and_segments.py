# Uses python3
import sys


def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    starts = list(zip(starts, [0] * len(starts), range(len(starts))))
    ends = list(zip(ends, [2] * len(ends), range(len(ends))))
    points = list(zip(points, [1] * len(points), range(len(points))))
    all = sorted(starts + ends + points, key= lambda x: (x[0], x[1]))
    lines = 0
    for loc, type, i in all:
        if type == 0:
            lines += 1
        elif type == 2:
            lines -= 1
        else:
            cnt[i] = lines
    return cnt


def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt


if __name__ == '__main__':
    # a = [1,2,3,5,6,7]
    # print(binary_search(a, 4))
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    # use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
