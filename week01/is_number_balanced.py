def is_number_balanced(number):
    digits_count=len(str(number))
    middle=digits_count//2 + 1 if digits_count%2!=0 else digits_count//2

    if digits_count==1:
        return True

    digits = [int(digit) for digit in str(number)]

    first_half=digits[:middle]
    second_half=digits[middle:]

    return sum(first_half)==sum(second_half)
