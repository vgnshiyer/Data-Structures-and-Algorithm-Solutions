'''
Reference: https://medium.com/@aiswaryamathur/find-the-n-th-permutation-of-an-ordered-string-using-factorial-number-system-9c81e34ab0c8

Given a string 'abcd', find the kth lexicographical permutation of the string.

Before jumping in to the solution, we need to understand the factorial number system. Instead of powers of 2/10 as in binary or decimal number system, the factorial number system uses factorials. The digit at the 0th place can take only one value. The digit at ones place can take 2 values and so on. So the digit at the nth place can take n+1 values.

For example, a number 349 in factoradic form is 242010. We progressively divide the number by 1, 2, 3, 4, 5 and so on until we get 0. The remainders are the digits of the number in factoradic form.

There is a direct relationship between permutations of strings and factorial number system.
While finding the nth lexicographical permutation of a string, if we convert n in to its factoradic form, the digits of the factoradic form will be the indices of the characters of the string in the nth permutation.

So 349th permutation of 'abcd' will be formed by extracting the elements at indices 2, 4, 2, 0, 1 from the string 'abcd'.
'''

import itertools

def get_factoradic(n):
    factoradic = [0] * 13
    i = 1
    while n != 0:
        factoradic[12 - i] = n % i
        n //= i
        i += 1
    return factoradic

def get_permutation(char_list, factoradic):
    char_list.sort()
    result = []
    used = [False] * len(char_list)

    for f in factoradic:
        pos = f
        c = get_unused_char_at_pos(char_list, pos, used)
        result.append(c)

    return ''.join(result)

def get_unused_char_at_pos(char_list, pos, used):
    count = -1
    for i in range(len(char_list)):
        if not used[i]:
            count += 1
            if count == pos:
                used[i] = True
                return char_list[i]
    return ' '

# Example usage:
str_input = "abcde"  # Replace with your input string
n = 10  # Replace with the desired factoradic number
char_list = list(str_input)
factoradic = get_factoradic(n)
permutation = get_permutation(char_list, factoradic)
print(permutation)
