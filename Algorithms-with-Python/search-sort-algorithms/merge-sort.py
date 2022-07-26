def merge_arrays(left, right):

    result = [None] * (len(left) + len(right))
    l_index = 0
    r_index = 0
    result_index = 0

    while l_index < len(left) and r_index < len(right):
        if left[l_index] < right[r_index]:
            result[result_index] = left[l_index]
            l_index += 1
        else:
            result[result_index] = right[r_index]
            r_index += 1
        result_index += 1

    while l_index < len(left):
        result[result_index] = left[l_index]
        l_index += 1
        result_index += 1

    while r_index < len(right):
        result[result_index] = right[r_index]
        r_index += 1
        result_index += 1

    return result


def merge_sort(nums):
    if len(nums) == 1:
        return nums

    middle = len(nums) // 2
    left = nums[:middle]
    right = nums[middle:]

    return merge_arrays(merge_sort(left), merge_sort(right))


numbers = [int(x) for x in input().split()]

print(*merge_sort(numbers))