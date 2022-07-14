import subprocess

EXE_STR = '#!/usr/bin/python3'
SOURCE_FILE = 'dz1_1.py'
RESULT_FILE = 'dz1_run.py'

pwd = subprocess.run(f'pwd', capture_output=True, text=True)
curr_dir = pwd.stdout.strip()

file_exist = subprocess.run(f'test -e "{RESULT_FILE}"', cwd=curr_dir, shell=True, capture_output=True)
if file_exist.returncode == 0:
    subprocess.run(f'rm {RESULT_FILE}', cwd=curr_dir, shell=True)

command_str = f'(echo \'{EXE_STR}\'; cat {SOURCE_FILE}) > {RESULT_FILE}'
subprocess.run(command_str, cwd=curr_dir, shell=True)

subprocess.run(['chmod', 'go-rwx', RESULT_FILE])

subprocess.run(['chmod', 'u+rx', RESULT_FILE])

subprocess.run(f'./{RESULT_FILE}', shell=True)