#!/usr/bin/env checkio --domain=py run split-pairs

# Split the string into pairs of two characters. If the string contains an odd number of characters, then the missing second character of the final pair should be replaced with an underscore ('_').
# 
# Input:A string.
# 
# Output:An iterable of strings.
# 
# Precondition:0<=len(str)<=100
# 
# 
# END_DESC

def split_pairs(a):
    list_a=list(a)
    len_str=len(a)
    if len_str == 0:
        #len=0
        split_str = list_a
    elif len_str == 1:
        #len = 1
        list_a[0]=list_a[0]+'_'
        split_str = list_a
    else:
        if len_str%2 == 0:
            #par
            split_str=[]
            pair_len_str=int(len_str/2)
            for i in range(pair_len_str):
                split_str.append(list_a[2*i] + list_a[2*i+1])
        else:
            #impar
            split_str=[]
            pair_len_str=int(len_str/2)
            for i in range(pair_len_str):
                split_str.append(list_a[2*i] + list_a[2*i+1])
            split_str.append(list_a[2*(i+1)] + '_')
        pass
    return split_str


if __name__ == '__main__':
    print("Example:")
    print(list(split_pairs('abcd')))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(split_pairs('abcd')) == ['ab', 'cd']
    assert list(split_pairs('abc')) == ['ab', 'c_']
    assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    assert list(split_pairs('a')) == ['a_']
    assert list(split_pairs('')) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")