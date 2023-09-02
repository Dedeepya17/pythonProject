import re

string = 'This is my 1st  program 2345.'



result = re.split("\d", string, 1)
print(result)