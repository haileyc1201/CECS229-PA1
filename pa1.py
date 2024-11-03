"""Hailey Clark CECS 229 PA1"""

""" ---------------- PROBLEM 1 ----------------"""


def equiv_to(a, m, low, high):
    #setting the lowest integer k in the given range that fulfills m*k = x-a
    k_low = int((low-a)/m) 
    
    #if the casted integer lowest k is less than the actual lowest k, then we add 1 to the lowest k
    if k_low < ((low-a)/m): 
        k_low += 1

    #setting the highest integer k in the given range that fulfills m*k = x-a
    k_high = int((high-a)/m) 
    
    #if the casted integer highest k is greater than the actual highest k, then we subtract 1 to the highest k
    if k_high > ((high-a)/m):
        k_high -= 1
    
    #creating a list of all the k values in the given range
    k_vals = list(range(k_low, k_high + 1))
    
    #creating a list of all the x values in the given range using x = a + k*m
    x_vals = [a + k * m for k in k_vals]
    
    #returning the list of x values
    return x_vals


""" ---------------- PROBLEM 2 ----------------"""


def b_rep(n, b):
    digits = []  # stores the digits of the b-representation of n
    q = n
    while q != 0:
        digit = int(q % b)
        if b == 16 and digit > 9:
            hex_dict = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
            digits.insert(0, hex_dict[digit])

        else:
            digits.insert(0, str(digit))
        q = (q-digit)/b
    return ''.join(digits)


""" ---------------- PROBLEM 3 ----------------"""


def binary_add(a, b):
    # removing all whitespace from the strings
    a = a.replace(' ', '')
    b = b.replace(' ', '')

    # padding the strings with 0's so they are the same length
    if len(a) < len(b):
        diff = len(b) - len(a)
        a = "0" * diff + a
    elif len(a) > len(b):
        diff = len(a) - len(b)
        b = "0" * diff + b

    # addition algorithm
    result = ""
    carry = 0
    for i in reversed(range(len(a))):
        a_i = int(a[i])
        b_i = int(b[i])

        result = str((a_i + b_i + carry) % 2) + result
        carry = (a_i + b_i + carry) // 2
    if carry == 1:
        result = "1" + result
    return result


""" ---------------- PROBLEM 4 ----------------"""


def binary_mul(a, b):
    # removing all whitespace from the strings
    a = a.replace(' ', '')
    b = b.replace(' ', '')

    # multiplication algorithm
    partial_products = []
    i = 0  # index of the current bit of string 'a' beginning at 0, right-to-left
    for bit in reversed(a):
        if bit == '1':
            partial_products.append(b + '0' * i)
        i += 1

    result = '0'
    while len(partial_products) > 0:
        result = binary_add(result, partial_products.pop())
    return  result