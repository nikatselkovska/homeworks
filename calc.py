print('Hello! I am ridiculous calculator.')
INT_LINK = 'https://en.wikipedia.org/wiki/Integer'
TEXT_ERROR = 'It is not an integer! See what integer is: ' + INT_LINK
OPERATION_TYPES = '+, -, /, *, +++'
entered_numbers = []
while True:
    first_number = input('Put first integer operand please: ')
    if first_number == '':
        continue 
    try:
        first_number = int(first_number)
        entered_numbers.append(first_number)
    except ValueError:
        print(TEXT_ERROR)
        continue
    break

while True:
    operation_type = input(f'Choose operation type please (only {OPERATION_TYPES}): ')
    if operation_type == '':
        continue
    elif all((len(operation_type) != 1 or operation_type not in '+-/*', operation_type != '+++')):
        print(f'There are only {OPERATION_TYPES}. Please input one of avalaible operations')
        continue
    break

its_multiple_sum = operation_type == '+++'
if its_multiple_sum:
    operation_type = '+'

while True:
    second_number = input('Put one more integer operand please: ')
    if second_number == '':
        if its_multiple_sum:
            break
        else:
            continue
    try:
        second_number = int(second_number)
        entered_numbers.append(second_number)
    except ValueError:
        print(TEXT_ERROR)
        continue
    if its_multiple_sum:
        continue
    else:
        break

result_num = 0
operands_str = ''
for entered_number in entered_numbers:
    if entered_numbers.index(entered_number) == 0:
        result_num = entered_number
    else: 
        if operation_type == '+':
            result_num += entered_number
        elif operation_type == '-':
            result_num -= entered_number
        elif operation_type == '/':
            try:
                result_num /= entered_number
            except ZeroDivisionError as err:
                print('There is an error:', err)
                quit()
        elif operation_type == '*':
            result_num *= entered_number
    operation_str = f' {operation_type} ' if entered_numbers.index(entered_number) != len(entered_numbers) - 1 else ''
    operands_str += str(entered_number) + operation_str

result_str = f'{operands_str} = {result_num}'
if operands_str:
    print(result_str)
else:
    print('There is unexpectable runtime error, we will improve it in later version...')
