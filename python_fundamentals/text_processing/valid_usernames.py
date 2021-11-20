words = input().split(', ')

for i in range(len(words)):
    if words[i].isalnum() and len(words[i]) > 3:

        print(words[i])

    elif "-" in words[i] and len(words[i]) > 3:
        temp_word = words[i].split('-')
        temp_word = '1'.join(temp_word)
        if temp_word.isalnum():
            temp_word = list(temp_word)
            for j in range(len(temp_word)):
                if temp_word[j] == "1":
                    temp_word.pop(j)
                    temp_word.insert(j, '-')
        print(words[i])

    elif "_" in words[i] and len(words[i]) > 3:
        temp_word = words[i].split('_')
        temp_word = '1'.join(temp_word)
        if temp_word.isalnum():
            temp_word = list(temp_word)
            for j in range(len(temp_word)):
                if temp_word[j] == "1":
                    temp_word.pop(j)
                    temp_word.insert(j, '_')
        print(words[i])
