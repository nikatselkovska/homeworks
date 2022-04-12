stress_level = ''
while True:
    stress_level = input('What is your stress level?')
    try:
        stress_level = int(stress_level)
    except Exception:
        print('Put some int!')
        continue
    if stress_level == 0:
        print('Your mental health is well. Glory to Ukraine!')
    elif stress_level < 0:
        print('Good for you...')
    else:
        final_str = 'A' * stress_level + '!'
        print(final_str)
    break