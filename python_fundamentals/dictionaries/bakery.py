string_val = input().split()
my_dict = {}

for i in range(0, len(string_val), 2):
    my_dict_key = string_val[i]
    my_dict_val = int(string_val[i+1])
    my_dict[my_dict_key] = my_dict_val

print(my_dict)
