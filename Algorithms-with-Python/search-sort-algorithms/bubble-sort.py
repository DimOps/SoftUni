def bubble_sort(nums):
    is_sorted = False
    filled_pos = 0
    while not is_sorted:
        is_sorted = True
        for i in range(1, len(nums) - filled_pos):  # takes a pair
            if nums[i] < nums[i - 1]:
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
                is_sorted = False  # if sort done on i-th iter., continue
        filled_pos += 1
    return nums


numbers = [int(x) for x in input().split()]

print(bubble_sort(numbers))
