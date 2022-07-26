def insertion_sort(nums):
    for i in range(1, len(nums)):  # second of two vals as comparator

        for j in range(i, 0, -1):  # backwards vals comparison

            if nums[j] < nums[j-1]:
                nums[j], nums[j - 1] = nums[j-1], nums[j]

    return nums


numbers = [int(x) for x in input().split()]

print(insertion_sort(numbers))