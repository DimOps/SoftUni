import re
string = input()

regex = r"(\+359 2 \d{3} \d{4})|(\+359-2-\d{3}-\d{4})"

matches = re.finditer(regex, string)

phones = [match.group() for match in matches]

print(', '.join(phones))
