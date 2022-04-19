print('Hello! I am ridiculous calculator.')
INT_LINK = 'https://en.wikipedia.org/wiki/Integer'
TEXT_ERROR = 'It is not an integer! See what integer is: ' + INT_LINK
while True:
    first_number = input('Put first integer operand please: ')
    try:
        first_number = int(first_number)
    except ValueError:
        print(TEXT_ERROR)
        continue
    break

while True:
    operation_type = input('Choose operation type please (only +, -, /, *): ')
    if operation_type not in '+-/*':
        print('There are only +, -, /, *. Please input one of avalaible operations')
        continue
    break

while True:
    second_number = input('Put second integer operand please: ')
    try:
        second_number = int(second_number)
    except:
        print(TEXT_ERROR)
        continue
    break

# for place economy we won't do if-elif-else construction, we will try to execute code as it is
str_execute = str(first_number) + str(operation_type) + str(second_number)
# str_result = "result = " + str_execute + "\nprint(" + '"' + str_execute + ' = "' + " + str(result))"
str_result = "result = {}\nprint({} + str(result))"
str_result = str_result.format(str_execute, '"' + str_execute + ' = "')
try:
    exec(str_result)
except Exception as err:
    print('Oops, there is some runtime error:', err)