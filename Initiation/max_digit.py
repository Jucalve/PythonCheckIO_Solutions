#!/usr/bin/env checkio --domain=py run max-digit

# You have a number and you need to determine which digit in this number is the biggest.
# 
# Input:A positive int.
# 
# Output:An Int (0-9).
# 
# 
# END_DESC

def max_digit(number: int) -> int:
    # your code here
    str_number = str(number)
    iter_number = iter(int(x) for x in str_number)
    return max(iter_number)


if __name__ == '__main__':
    print("Example:")
    print(max_digit(0))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert max_digit(0) == 0
    assert max_digit(52) == 5
    assert max_digit(634) == 6
    assert max_digit(1) == 1
    assert max_digit(10000) == 1
    print("Coding complete? Click 'Check' to earn cool rewards!")