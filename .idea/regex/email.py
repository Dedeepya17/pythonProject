import re

def solve(s):
   x = "^[a-zA-Z0-9-\.]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
   if re.match(x,s):
      return True
   return False

s = "ch.dedeepya17@gmail.com"
print(solve(s))