import re

pattern = r'^[a-z]+_[a-z]+'
test_strings = ['hello_world', 'Python_code', 'Hello_World', 'test_case']

for s in test_strings:
    if re.search(pattern, s):
        print(f"Found: {s}")
