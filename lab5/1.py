import re

pattern = r'ab*'
test_strings = ['a', 'ab', 'abb', 'ac', 'b']

for s in test_strings:
    if re.fullmatch(pattern, s):
        print(f"Match: {s}")
