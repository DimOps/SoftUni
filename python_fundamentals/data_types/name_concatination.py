def string_concatenation(first_str, second_str, delimiter):

    storage_list = [first_str, delimiter, second_str]
    concatenated_str = ''.join(storage_list)
	
    print(concatenated_str)

beginning = input()
end = input()
delim = input()

string_concatenation(beginning, end, delim)
