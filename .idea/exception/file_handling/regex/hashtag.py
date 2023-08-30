import re
text =' This #can be done by #writing the newline'
hashtags=re.findall(r'#\w+',text)
print(hashtags)