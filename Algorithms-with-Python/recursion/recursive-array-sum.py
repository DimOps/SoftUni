def calc_sum(vals, index):
    if index == len(vals) - 1:
        return vals[index]

    return vals[index] + calc_sum(vals, index + 1)


nums = [int(x) for x in input().split()]  # Input: 1 2 3 4

print(calc_sum(nums, 0))  # Output: 10 on the console