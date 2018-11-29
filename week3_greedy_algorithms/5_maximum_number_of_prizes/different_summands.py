# Uses python3
import sys

def optimal_summands(n):
    summands = []
    #write your code here
    current = 0
    while (n > current):
        current += 1
        if n - current > current:
            summands.append(current)
            n -= current
        else:
            summands.append(n)
            n = 0

    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
