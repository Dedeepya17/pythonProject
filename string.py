#.string returns the string passed into the function
import re

txt = "This is my program"
x = re.search(r"\bp\w+", txt)
print(x.string)