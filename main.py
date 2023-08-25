import config
import os
import cleardata

cleardata.cleardata('fakeinfo')

answer = input('Have you setup the mail server[y/N]: ')

if answer.lower().strip() == 'y' or answer.lower().strip() == 'yes':
    if config.parallel:
        with open("runcreator.py") as f:
            exec(f.read())
        os.system('bash run.sh')
    else:
        with open("abuse.py") as f:
            exec(f.read())
else:
    print('Please setup the mail server and run again')
