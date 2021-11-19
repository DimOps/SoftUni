def smallest_num(sequence):
    from sys import maxsize

    comp = maxsize

    for i in range(len(sequence)):

        if sequence[i] < comp:
            comp = sequence[i]
    print(comp)

	
numbers = []

for _ in range(0, 3):

    digit = int(input())
    numbers.append(digit)
	
smallest_num(numbers)
