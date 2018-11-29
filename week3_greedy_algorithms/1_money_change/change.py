# Uses python3
import sys

def get_change(m):
    #write your code here
    count = 0
    coin_index = 0 
    coins = [10, 5, 1]
    while (m > 0):
        if (m - coins[coin_index] >= 0):
            count += 1
            m = m - coins[coin_index]
        else:
            coin_index += 1
            if (coin_index >= len(coins)):
                return count
    return count

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
