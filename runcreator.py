import config

with open('run.sh', 'w') as f:
    pname = config.pyname+' abuse.py'
    amount = config.processes
    
    execstr = ''
    for i in range(amount):
        execstr = execstr + pname + ' & '
    execstr = execstr[:-3]   
    f.write("(trap 'kill 0' SIGINT; " + execstr + ")")
