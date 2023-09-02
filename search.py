import re

txt = "This is my program"
x = re.search("my", txt)
print(x)
if re.match:
  print("pattern found inside the string")
else:
  print("pattern not found")