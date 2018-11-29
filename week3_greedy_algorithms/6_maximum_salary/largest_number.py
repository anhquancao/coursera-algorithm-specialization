#Uses python3

import sys

def isGreaterOrEqual(digit, maxDigit):
    return int(digit + maxDigit) > int(maxDigit + digit)

def largest_number(a):
    #write your code here
    res = ""
    if (len(a) == 0):
        return ""

    while (len(a) > 0):
        maxDigit = a[0]
        for digit in a:
            if isGreaterOrEqual(digit, maxDigit):
                maxDigit = digit
        res += maxDigit
        # print(a, maxDigit)
        a.remove(maxDigit)

    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
