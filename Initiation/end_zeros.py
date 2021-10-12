#!/usr/bin/env checkio --domain=py run end-zeros

# Try to find out how many zeros a given number has at the end.
# 
# Input:A positive Int
# 
# Output:An Int.
# 
# 
# END_DESC

def end_zeros(num: int) -> int:
    stra = str(num)
    a=0
    s=1
    while (stra[len(stra)-s] == "0"):
        a=a+1
        if s==len(stra):    
            break
        else:
            s=s+1
    return a


if __name__ == '__main__':
    print("Example:")
    print(end_zeros(0))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert end_zeros(0) == 1
    assert end_zeros(1) == 0
    assert end_zeros(10) == 1
    assert end_zeros(101) == 0
    assert end_zeros(245) == 0
    assert end_zeros(100100) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")