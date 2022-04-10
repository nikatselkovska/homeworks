stressLevel = ''
while True:
    stressLevel = input('What is your stress level?')
    try:
        stressLevel = int(stressLevel)
    except:
        print('Put some int!')
        continue
    if stressLevel == 0:
        print('Your mental health is well. Glory to Ukraine!')
    elif stressLevel < 0:
        print('Good for you...')
    else:
        finalStr = 'A' * stressLevel + '!'
        print(finalStr)
    break

