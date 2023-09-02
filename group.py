#.group() returns the part of the string where there was a match
#The regular expression looks for any words that starts with an upper case "P"
import re

txt = "This is my Program"
x = re.search(r"\bP\w+", txt)
print(x.group())