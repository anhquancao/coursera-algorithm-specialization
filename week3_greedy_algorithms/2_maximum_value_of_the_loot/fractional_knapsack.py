# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    total_value = 0.
    vws = []
    # write your code here
    for i in range(len(weights)):
        vw = values[i] / weights[i]
        vws.append(vw)
    while (capacity > 0 and len(weights) > 0):    
        max_vw = max(vws)
        index = vws.index(max_vw)
        weight = weights[index]
        value = values[index]

        if (weight < capacity):
            capacity -= weight
            total_value += value
            weights.pop(index)
            values.pop(index)
            vws.pop(index)
        else:
            total_value += capacity * max_vw
            capacity = 0
            

    return total_value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
