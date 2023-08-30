import re
text=" she-had example and another weh-ad."
hypened_word=re.findall(r'\b\w+-\w+\b',text)
print(hypened_word)