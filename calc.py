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
    second_number = input('Put second integer operand please: ')
    try:
        second_number = int(second_number)
    except:
        print(TEXT_ERROR)
        continue
    break

int_result = first_number + second_number
str_resut = str(first_number) + ' + ' + str(second_number) + ' = ' + str(int_result)
print(str_resut)