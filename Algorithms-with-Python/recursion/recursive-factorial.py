def solve_factorial(val):

    if val == 0:  # recursive depth is reached
        return 1  # const for 0!

    return val * solve_factorial(val-1)


n = int(input())

print(solve_factorial(n))