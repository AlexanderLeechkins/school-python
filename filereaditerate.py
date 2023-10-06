import re

with open("stringvalidator.py", "r") as file:
    text= file.read()

match= re.finditer("(?:print[(])(.*)(?:[)])",text)
print(match)
for i in match:
    for group in i.groups():
        print(group)
        