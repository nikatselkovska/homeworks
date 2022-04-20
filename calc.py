print('Hello! I am ridiculous calculator.')
INT_LINK = 'https://en.wikipedia.org/wiki/Integer'
TEXT_ERROR = 'It is not an integer! See what integer is: ' + INT_LINK
while True:
    first_number = input('Put first integer operand please: ')
    if first_number == '':
        continue 
    try:
        first_number = int(first_number)
    except ValueError:
        print(TEXT_ERROR)
        continue
    break

while True:
    operation_type = input('Choose operation type please (only +, -, /, *): ')
    if operation_type == '':
        continue
    elif len(operation_type) != 1 or operation_type not in '+-/*':
        print('There are only +, -, /, *. Please input one of avalaible operations')
        continue
    break

while True:
    second_number = input('Put second integer operand please: ')
    if second_number == '':
        continue
    try:
        second_number = int(second_number)
    except ValueError:
        print(TEXT_ERROR)
        continue
    break

result_num = None
if operation_type == '+':
    result_num = first_number + second_number
elif operation_type == '-':
    result_num = first_number - second_number
elif operation_type == '/':
    try:
        result_num = first_number / second_number
    except ZeroDivisionError as err:
        print('There is an error:', err)
        quit()
elif operation_type == '*':
    result_num = first_number * second_number

result_str = f'{first_number} {operation_type} {second_number} = {result_num}'
if result_num:
    print(result_str)
else:
    print('There is unexpectable runtime error, we will improve it in later version...')
