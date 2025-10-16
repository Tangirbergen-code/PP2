import re

text = "Python, regex. is fun to learn"
replace = re.sub(r'[ ,.]',":", text)
print(replace)