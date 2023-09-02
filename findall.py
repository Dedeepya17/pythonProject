
# Program to extract numbers from a string

import re

string = 'hello 12 world 89. This is 34'
pattern = '\d+'

result = re.findall(pattern, string)
print(result)


