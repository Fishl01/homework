def is_palindrome(word: str) -> bool:
    word = word.replace(" ", "").lower()
    return True if word[::-1] == word else False


print(is_palindrome("p eOp le "))  # False
print(is_palindrome("A b o ba"))  # True
