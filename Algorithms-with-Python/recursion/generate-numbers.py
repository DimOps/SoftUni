def generate_numbers(index, vect):

    if index == len(vect):
        print(*vect, sep=' ')
        return

    for num in range(1, n + 1):
        vect[index] = num
        generate_numbers(index + 1, vect)


n = int(input())

vector = [0] * n

generate_numbers(0, vector)