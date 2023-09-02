import re
def regex(d):
    return re.search("(20|19|18|17)\d{2}/(0[1-9]|1[0-2])/(0[0-9]|1[0-9]|2[0-9]|3[0-1])",d)
d="1869/12/16"
print(regex(d))
#