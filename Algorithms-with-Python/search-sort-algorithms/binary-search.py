def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1
    while left <= right:
        middle_index = (left + right) // 2
        mid_el = numbers[middle_index]
        if mid_el == target:
            return middle_index

        if target > mid_el:
            left = middle_index + 1
        else:
            right = middle_index - 1

    return -1


nums = [int(x) for x in input().split()]

t = int(input())

print(binary_search(nums, t))
