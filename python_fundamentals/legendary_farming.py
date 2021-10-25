data = []

br = ''
items = []
item_quantity = []
dict_of_items = {}

check_list = ['motes', 'fragments', 'shards']

for word in check_list:
    if word not in dict_of_items:
        dict_of_items[word] = 0

while br == '':

    data = input().split()
    items = []
    item_quantity = []
    [(items.append(data[i + 1]), item_quantity.append(int(data[i]))) for i in range(0, len(data), 2)]

    items = [word.lower() for word in items]


    for k in range(len(items)):

        if items[k] not in dict_of_items:
            dict_of_items[items[k]] = 0

        dict_of_items[items[k]] += item_quantity[k]

        if dict_of_items['motes'] >= 250:
		
            dict_of_items['motes'] -= 250
            print("Dragonwrath obtained!")
            br = 'break'
            break
			
        if dict_of_items['shards'] >= 250:
		
            dict_of_items['shards'] -= 250
            print("Shadowmourne obtained!")
            br = 'break'
            break
			
        if dict_of_items['fragments'] >= 250:
		
            dict_of_items['fragments'] -= 250
            print("Valanyr obtained!")
            br = 'break'
            break


split_idx = 3
dict1 = dict(list(dict_of_items.items())[:split_idx])
dict2 = dict(list(dict_of_items.items())[split_idx:])

sorted_dict1 = dict(sorted(dict1.items(), key=lambda x: (-x[1], x[0])))
sorted_dict2 = dict(sorted(dict2.items(), key=lambda x: (x[0], x[1])))

dictionary = {}
dictionary.update(sorted_dict1)
dictionary.update(sorted_dict2)

for key, value in dictionary.items():

    print(f'{key}: {value}')
