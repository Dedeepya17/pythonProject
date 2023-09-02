import re

string = 'hello world python '
pattern = '\d+'

result = re.findall(pattern, string)
print(result)