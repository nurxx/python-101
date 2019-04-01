from palindrome import palindrome

def get_largest_palindrome(n):
    numbers=list(reversed(range(n)))
    for item in numbers:
        if palindrome(item)==True:
            return item
