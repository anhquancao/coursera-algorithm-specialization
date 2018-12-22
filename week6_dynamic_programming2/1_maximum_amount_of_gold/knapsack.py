# Uses python3
import sys


def optimal_weight(W, w):
    v = [[0 for x in range(W + 1)] for y in range(len(w) + 1)]
    for cur_w in range(1, W + 1):
        for i in range(1, len(w) + 1):
            v[i][cur_w] = v[i - 1][cur_w]
            if w[i - 1] <= cur_w:
                temp = v[i - 1][cur_w - w[i - 1]] + w[i - 1]
                if temp > v[i][cur_w]:
                    v[i][cur_w] = temp
    return v[len(w)][W]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    # W = 10
    # n = 3
    # w = [1, 4, 8]
    print(optimal_weight(W, w))
