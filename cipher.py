UPPER_ORD = tuple(range(ord('A'), ord('Z') + 1))
LOWER_ORD = tuple(range(ord('a'), ord('z') + 1))


def encode_symbol(first, last, symbol, key):
    res = first + (symbol - first + key) % (last - first + 1)
    return res


encryption_mode = input('Enter 0 for decryption or 1 for encryption: ')
if all((encryption_mode != '0', encryption_mode != '1')):
    print('Your input data is incorrect, please try again.')
    exit()
encryption_mode = bool(int(encryption_mode))

while True:
    text_message = input('Enter text message (only [aA-zZ]): ')
    if text_message:
       break

shift_value = input('Enter shift value (only integer): ')
try:
    shift_value = int(shift_value)
except ValueError as err:
    print(f'Your input data is incorrect ({err})')
    exit()

shift_value = shift_value if encryption_mode else -shift_value

final_message = ''
for text_symbol in text_message:
    final_symbol = text_symbol
    if text_symbol.isalpha():
        current_ord_tuple = UPPER_ORD if text_symbol.isupper() else LOWER_ORD
        symbol_index = current_ord_tuple.index(ord(text_symbol))
        result_index = encode_symbol(0, len(current_ord_tuple)-1, symbol_index, shift_value)
        final_symbol = chr(current_ord_tuple[result_index])
    final_message += final_symbol

print(f'Result: {final_message}')