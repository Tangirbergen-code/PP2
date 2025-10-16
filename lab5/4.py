import re

pattern = r'[A-Z][a-z]+'
test_strings = ['Hello', 'Test', 'python', 'Code', 'ABC']

for s in test_strings:
    if re.fullmatch(pattern, s):
        print(f"Match: {s}")
