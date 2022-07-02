import argparse
import uuid
import os
import requests
import random


parser = argparse.ArgumentParser(description='Getting kittens images')
parser.add_argument(
    'amount',
    type=int,
    default=1,
    help='images amount',
)
parser.add_argument(
    'out_dir',
    type=str,
    default=os.getcwd(),
    help='output directory',
)
parser.add_argument(
    '--grey',
    dest='grey',
    action='store_const',
    const=True,
    default=False,
    help='need to be grey'
)

args = parser.parse_args()
if args.amount <= 0:
    print('Incorrect parameter \'amount\':', args.amount)
    exit()

grey = 'g/' if args.grey else ''
out_dir = f'{args.out_dir}/' if args.out_dir[-1] != '/' else args.out_dir
try:
    os.makedirs(out_dir, exist_ok=True)
except OSError as err:
    print('Creating directory error: ', err)
    exit()

for i in range(args.amount):
    width = random.randint(100, 1000)
    height = random.randint(100, 1000)
    request_str = f'http://placekitten.com/{grey}{width}/{height}'
    response = requests.get(request_str)
    if response.status_code != 200:
        print(f'GET error: {response.status_code}', response.reason)
        continue
    file_name = f'kit_{uuid.uuid4()}'
    file = open(f'{out_dir}{file_name}.jpeg', 'wb')
    file.write(response.content)
    file.close()

print('Kittens are uploaded if there were no errors. Enjoy!')

