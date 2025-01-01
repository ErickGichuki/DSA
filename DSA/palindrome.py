# palindrome problem
# Given an integer x, return true if x is a palindrome, and false otherwise.

def pali(x):
    if x < 0:
        return False
    string_x = str(x)
    return string_x == string_x[::-1]
x = 122
print(pali(x))