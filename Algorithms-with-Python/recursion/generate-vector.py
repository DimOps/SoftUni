def generate_vector(index, vect):

    if index == len(vect):
        print(*vect, sep=' ')
        return

    for num in range(0, 2):  # two possible numbers in a cell (binary)
        vect[index] = num
        generate_vector(index + 1, vect)


n = int(input())

vector = [0] * n

generate_vector(0, vector)