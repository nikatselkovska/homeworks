import subprocess
import datetime
import calendar
import random

subprocess.run(f'whoami')
pwd = subprocess.run(f'pwd', capture_output=True, text=True)
curr_dir = pwd.stdout.strip()
print(curr_dir)

new_dir_name = 'dz1'
try:
    subprocess.check_call(f'mkdir {new_dir_name}', shell=True, cwd=curr_dir)
except subprocess.SubprocessError as err:
    print(err)

curr_date_time = datetime.datetime.now()
amount_days = calendar.monthrange(curr_date_time.year, curr_date_time.month)[1]
list_files = [datetime.date(curr_date_time.year, curr_date_time.month, day).strftime('%d-%m-%Y') for day in range(1, amount_days+1)]
for filename in list_files:
    subprocess.run(f'touch {filename}.log', cwd=new_dir_name, shell=True)

new_owner = 'root'
subprocess.run(f'sudo -S chown {new_owner} {new_dir_name}', cwd=curr_dir, shell=True)

curr_dir_dz = curr_dir + '/' + new_dir_name
for delete_file in random.sample(list_files, 5):
    subprocess.run(f'rm {delete_file}.log', cwd=curr_dir_dz, shell=True)
    print(f'{delete_file} was deleted')