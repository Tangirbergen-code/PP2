import  re 

pattern = r'a.*b'
test_strings = ['ab', 'acb', 'a123b', 'accbb', 'a-b']

for s in test_strings:
    if re.fullmatch(pattern, s):
        print(f"Match: {s}")
