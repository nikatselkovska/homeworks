def check_cucumber(cucumber):
    assert cucumber, 'there is empty input'
    assert cucumber.find(' ') == -1, 'there are excess spaces'
    assert cucumber[0].isupper(), 'the first symbol should be upper'
    assert cucumber[1:].islower(), 'the symbols after first symbol should be lower'
    assert cucumber == 'Cucumber', 'it is something else, not a Cucumber'


print('Hi!')
while True:
    input_cucumber = input('Enter please the word \'Cucumber\':')
    try:
        check_cucumber(input_cucumber)
    except AssertionError as error:
        print(error)
        continue
    print('Thank you')
    break

