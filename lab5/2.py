import re

pattern = r'ab{2,3}'
test_strings = ['a', 'ab', 'abb', 'abbb', 'abbbb']

for s in test_strings:
    if re.fullmatch(pattern, s):
        print(f"Match: {s}")
