class Operations:

    def add(self, *iters):
        return sum(iters)

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        result = None
        try:
            result = a / b
        except ZeroDivisionError:
            print('♾ (infinity)')
            quit()
        return result

    def sub(self, a, b):
        return a - b


class Calc:

    oper = Operations
    entered_numbers = []
    current_operation = None
    result_number = None
    operands_str = ''
    multiple_arg = False

    def say_hi(self):
        print('Hello! I am ridiculous calculator.')

    def __init__(self):
        self.say_hi()

    def clear_all(self):
        self.entered_numbers.clear()
        self.current_operation = None
        self.result_number = None
        self.operands_str = ''
        self.multiple_arg = False

    def execute_operation(self, show_message=False):
        self.result_number = self._OPERATION_TYPES[self.current_operation](self.oper, *self.entered_numbers)
        if show_message:
            for i, entered_number in enumerate(self.entered_numbers):
                operation_str = f' {self.current_operation} ' if i != len(self.entered_numbers) - 1 else ''
                self.operands_str += str(entered_number) + operation_str

            result_str = f'{self.operands_str} = {self.result_number}'
            if self.operands_str:
                print(result_str)
            else:
                print('There is unexpectable runtime error, we will improve it in later version...')
        return self.result_number

    def input_number(self, input_message, multiple=False):
        text_error = 'It is not an integer or float!'
        number = None
        while True:
            number = input(input_message)
            if number == '':
                if multiple:
                    return number
                continue
            try:
                number = float(number)
            except ValueError:
                print(text_error)
                continue
            break
        self.entered_numbers.append(number)
        return number

    def input_operation(self):
        keys_operations = list(self._OPERATION_TYPES.keys())
        while True:
            operation_type = input(f'Choose operation type please {keys_operations}: ')
            if operation_type == '':
                continue
            elif operation_type not in keys_operations:
                print(f'There are only {keys_operations}. Please input one of avalaible operations')
                continue
            break
        self.multiple_arg = (operation_type == '+++')
        self.current_operation = operation_type if not self.multiple_arg else '+'
        return operation_type

    _OPERATION_TYPES = {
        '+': oper.add,
        '-': oper.sub,
        '/': oper.div,
        '*': oper.mul,
        '+++': oper.add,
    }


if __name__ == '__main__':
    magic_calc = Calc()
    magic_calc.input_operation()
    magic_calc.input_number('Put first numerical operand please: ')
    while True:
        num = magic_calc.input_number('Put one more numerical operand please: ', magic_calc.multiple_arg)
        if not magic_calc.multiple_arg or not num:
            break
    magic_calc.execute_operation(show_message=True)


