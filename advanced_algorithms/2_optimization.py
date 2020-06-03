import sys

def recursive_fibonacci(n):
    if n == 0 or n == 1:
        return 1

    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)


def recursive_fibonacci_mem(n, memo = {}):
    if n == 0 or n == 1:
        return 1

    try:
        return memo[n]
    except KeyError:
        result = recursive_fibonacci_mem(n - 1, memo) + recursive_fibonacci_mem(n - 2)
        memo[n] = result
        return result

if __name__ == '__main__':
    sys.setrecursionlimit(2200)
    n = int(input("Input a number: "))
    result = recursive_fibonacci_mem(n, {})
    print(result)