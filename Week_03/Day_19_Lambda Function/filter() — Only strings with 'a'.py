items = ["ameer", "ali", "bilal", "sara", "zain"]
# Checks if the character 'a' is present in the string
has_a = list(filter(lambda x: 'a' in x.lower(), items))
print(f"String with 'a': {has_a}")  