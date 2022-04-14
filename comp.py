print('Hello! I am ridiculous PORIVNYACH.')
# make some comfort for us at this stage of learning: limits for input data (only int and float -> only float)

TEXT_ERROR_NUM = "Can't recognize a number. PORIVNYACH accepts only integers and floating point numbers! Please, try again."

while True:
    first_number = input('Put first numeric operand please: ')
    # making float for all cases
    try:
        first_number = float(first_number)
    except ValueError:
        print(TEXT_ERROR_NUM)
        continue
    break

while True:
    second_number = input('Put second numeric operand please: ')
    # making float for all cases
    try:
        second_number = float(second_number)
    except ValueError:
        print(TEXT_ERROR_NUM)
        continue
    break

str_result = 'Sorry, unexpectable result of operation... We will include this case in PORIVNYACH 2.0'
if first_number == second_number:
    str_result = 'Numbers ' + str(first_number) + ' and ' + str(second_number) + ' are equal'
elif first_number > second_number:
    str_result = 'First number (' + str(first_number) + ') is bigger than second (' + str(second_number) + ')'
elif second_number > first_number:
    str_result = 'Second number (' + str(second_number) + ') is bigger than first (' + str(first_number) + ')'

print(str_result)