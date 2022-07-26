def selection_sort(nums):
    for i in range(len(nums)):
        min_number = nums[i]  # assumes the first number
        min_i = i
        for next_i in range(i + 1, len(nums)):
            next_number = nums[next_i]
            if next_number < min_number:
                min_number = next_number
                min_i = next_i
        nums[i], nums[min_i] = nums[min_i], nums[i]

    return nums


numbers = [int(x) for x in input().split()]

print(selection_sort(numbers))
