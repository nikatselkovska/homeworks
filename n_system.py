from typing import final

N_SYSTEM = 11

DICT = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11}


def convert_base(num, to_base=10, from_base=10):
    # first convert to decimal number
    try:
        n = int(num, from_base) if isinstance(num, str) else num
    except ValueError as err:
        print(f'Your input data is incorrect, please try again ({err})')
        return None
    # now convert decimal to 'to_base' base
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""
    while n > 0:
        n,m = divmod(n, to_base)
        res += alphabet[m]
    return res[::-1]


print(f'This is my {N_SYSTEM} numeric system')
for symb, value in DICT.items():
    print(f'{symb} = {value}')

input_num = input('Enter your number: ')
set_dif = set(input_num) - set(DICT.keys())
if set_dif:
    for symbol in set_dif:
        print(f'Symbol {symbol} is not from my numeric system')
    exit()

final_num = convert_base(input_num, from_base=N_SYSTEM)
if final_num:
    print(f'Final decimal number: {final_num}')


