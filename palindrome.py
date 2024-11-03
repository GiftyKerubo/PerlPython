def is_palindrome(word):
    return word == word[::-1]

print(is_palindrome("deified"))
print(is_palindrome("lemonade"))
print(is_palindrome("level"))
print(is_palindrome("phenomenon"))
print(is_palindrome("civic"))
