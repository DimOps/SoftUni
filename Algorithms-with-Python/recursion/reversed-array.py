def reverse_seq(vals, result, index):
    temp = vals.pop()
    result.append(temp)
    if len(result) - 1 == index:
        return result

    return reverse_seq(vals, result, index)


seq = [int(x) for x in input().split()]  # Input: 1 2 3 4
index = len(seq) - 1
r_seq = []
print(*reverse_seq(seq, r_seq, index))  # Output: '4 3 2 1' on the console