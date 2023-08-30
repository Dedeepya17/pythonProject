import re
def solve(s):
    regex='^[a-z 0-9]+@[a-z 0-9]+\.[a-z]{2,3}$'
    if re.match(regex,s):
        return True
    return False
s="chdedeepya17@gmail.com"
print(solve(s))