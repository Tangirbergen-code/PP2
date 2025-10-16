import re

text = "SplitThisStringAtUpperCase"
result = re.split(r'(?=[A-Z])', text)
print(result)
