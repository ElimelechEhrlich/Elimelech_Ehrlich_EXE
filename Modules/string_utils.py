def reverse_string(string):
    return string[::-1]


def is_palindrome(string):
    if reverse_string(string) == string:
        return True
    else:
        return False

