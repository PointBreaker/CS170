hex_key = ['0', '1']
def decimal_binary(d, digits):
    """
    return the binary representation of d using Karatsuba, digits is the length of
    the binary representation of d
    >>> decimal_binary(42, 6)
    '101010'
    >>> decimal_binary(10, 4)
    '1010'
    >>> decimal_binary(2 ** 12 + 2 **3 + 2 ** 2 + 2 ** 1 + 2 ** 0, 13)
    '1000000001111
    """
    if digits == 1:
        return hex_key[d]
    right_digit = digits // 2
    left_digit = digits - right_digit
    x_l = d >> right_digit
    x_r = d - (x_l << right_digit)
    # print("DEBUG:", d, x_l, x_r, digits, right_digit, left_digit)
    return decimal_binary(x_l, left_digit) + decimal_binary(x_r, right_digit)
