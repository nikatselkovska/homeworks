
print('Hello! I am ridiculous calculator.')
OPERATION_TYPES = ('+', '-', '/', '*', '+++')
entered_numbers = []


def input_number(input_message, multiple_sum):
    text_error = 'It is not an integer or float!'
    number = None
    while True:
        number = input(input_message)
        if number == '':
            if multiple_sum:
                break
            continue
        try:
            number = float(number)
        except ValueError:
            print(text_error)
            continue
        break
    return number


first_number = input_number('Put first numerical operand please: ', False)
entered_numbers.append(first_number)

while True:
    operation_type = input(f'Choose operation type please {OPERATION_TYPES}: ')
    if operation_type == '':
        continue
    elif operation_type not in OPERATION_TYPES:
        print(f'There are only {OPERATION_TYPES}. Please input one of avalaible operations')
        continue
    break

its_multiple_sum = operation_type == '+++'
if its_multiple_sum:
    operation_type = '+'

while True:
    second_number = input_number('Put one more numerical operand please: ', its_multiple_sum)
    if its_multiple_sum and second_number == '':
        break
    entered_numbers.append(second_number)
    if not its_multiple_sum:
        break


result_num = 0
operands_str = ''
for i, entered_number in enumerate(entered_numbers):
    if i == 0 or operation_type == '+':
        result_num += entered_number
    elif operation_type == '-':
        result_num -= entered_number
    elif operation_type == '/':
        try:
            result_num /= entered_number
        except ZeroDivisionError:
            print('♾ (infinity)')
            quit()
    elif operation_type == '*':
        result_num *= entered_number
    operation_str = f' {operation_type} ' if i != len(entered_numbers) - 1 else ''
    operands_str += str(entered_number) + operation_str

result_str = f'{operands_str} = {result_num}'
if operands_str:
    print(result_str)
else:
    print('There is unexpectable runtime error, we will improve it in later version...')