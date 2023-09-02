#.span() returns a tuple containing the start-, and end positions of the match

import re

txt = "This is my Program"
x = re.search(r"\bP\w+", txt)
print(x.span())