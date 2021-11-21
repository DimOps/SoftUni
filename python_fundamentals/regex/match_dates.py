
import re

string = input()


regex = r"(?P<day>\d{2})(?P<separator>[./-])(?P<month>[A-Z][a-z]{2})(?P=separator)(?P<year>\d{4})"

# the regex shows exclusivity with the separator

matches = re.finditer(regex, string)

date = [match.group() for match in matches]

for i in range(len(date)):

    sep_date = []

    if "/" in date[i]:

        sep_date = date[i].split('/')
        print(f'Day: {sep_date[0]}, Month: {sep_date[1]}, Year: {sep_date[2]}')

    elif "." in date[i]:

        sep_date = date[i].split('.')
        print(f'Day: {sep_date[0]}, Month: {sep_date[1]}, Year: {sep_date[2]}')

    elif "-" in date[i]:

        sep_date = date[i].split('-')
        print(f'Day: {sep_date[0]}, Month: {sep_date[1]}, Year: {sep_date[2]}')
