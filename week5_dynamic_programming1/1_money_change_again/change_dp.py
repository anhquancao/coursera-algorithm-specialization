# Uses python3
import sys



def get_change(m, s):
    coins = [1, 3, 4]

    if s[m] != -1:
        return s[m]

    min_change = sys.maxsize
    for coin in coins:
        if m - coin >= 0:
            change = 1 + get_change(m - coin, s)
            if change < min_change:
                min_change = change
    s[m] = min_change
    return s[m]


if __name__ == '__main__':
    m = int(sys.stdin.read())
    # m = 34
    s = [-1] * (m + 1)
    s[0] = 0
    print(get_change(m, s))
