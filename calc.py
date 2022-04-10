print('Hello! I am ridiculous calculator.')
intLink = 'https://en.wikipedia.org/wiki/Integer'
textError = 'It is not an integer! See what integer is: ' + intLink
while True:
    firstNumber = input('Put first integer operand please: ')
    try:
        firstNumber = int(firstNumber)
    except:
        print(textError)
        continue
    break

while True:
    secondNumber = input('Put second integer operand please: ')
    try:
        secondNumber = int(secondNumber)
    except:
        print(textError)
        continue
    break

intResult = firstNumber + secondNumber
strResut = str(firstNumber) + ' + ' + str(secondNumber) + ' = ' + str(intResult)
print(strResut)