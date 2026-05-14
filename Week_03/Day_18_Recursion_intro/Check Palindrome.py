def is_palindrome(s):
    if len(s) <= 1: # Base Case
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])
print(f"Is 'madam' a Palindrome?: {is_palindrome('madam')}")