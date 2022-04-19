DESIRED_STR = 'cucumber'

cuc_input = input(f'Please enter some text using word \'{DESIRED_STR}\': ')
index_cuc = cuc_input.find(DESIRED_STR)
if index_cuc != -1:
    print(cuc_input[index_cuc::])
else:
    print(f'Such a sad story that doesn\'t include {DESIRED_STR}... It\'s ruined my day.')