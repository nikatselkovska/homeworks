
print('Hello, dear friend!')
while True:
    str_input = input('Enter please some interesting text message for me: ')
    if str_input:
        break

str_dict = {}
for symbol in set(str_input):
    str_dict[symbol] = str_input.count(symbol)

for symbol, count in str_dict.items():
    print(f'\'{symbol}\' is counted {count} times')
