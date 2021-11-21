import re
pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"
text = input()
mates = re.finditer(pattern, text)
for mat in mates:
	print(mat.group(0), end=" ")
