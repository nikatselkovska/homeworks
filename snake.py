import time
import random

RANGE = 100
print('Hello! I hope you\'re well. This is a ~SnAkE pRoGrAm~')

randint = random.randint(0, RANGE)
while True:
    time.sleep(0.1)
    str_distance = ' ' * randint
    try:
        print(f'{str_distance}*')
    except KeyboardInterrupt:
        break
    randint = randint + random.randint(-1, 1)

print('0_0')
