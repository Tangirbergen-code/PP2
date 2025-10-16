import re

text = "camelCaseToSnakeCase"
result = re.sub(r'([A-Z])', r'_\1', text).lower()
print(result)
