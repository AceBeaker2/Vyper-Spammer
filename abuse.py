# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 16:29:15 2023

@author: skynet
"""
import time
import os
import re
import asyncio
import vyperapi
from multiprocessing import Process
from random import randint
import sys
import config

verbose = '-v' in sys.argv

if verbose:
    config.processes = 1
#ref_link = input("Input referral link: ")

async def abuse(email,name):
    vyperapi.send_api(email, name)

    filename = 'maildata/' + email.split('@')[0] + '.txt'
    done = False

    while not done:
        if os.path.isfile(filename):
            done = True

    with open(filename, "r") as file:
        lines = file.readlines()

    textdata = ''
    for line in lines:
        textdata = textdata + '\n' + line

    match = re.search(r"\((.*?)\)", textdata)
    link = match.group(1)
    #os.system('python3.9 fire_forget.py ' + link + ' &')
    vyperapi.get(link)

import fakeinfo

counter = 0

fakedata = fakeinfo.savefakes()

print('[Status] Fakes stored in ' + fakedata)

with open(fakedata, "r") as f:
    lines = f.readlines()

start = time.time()

# To stop network spam by ensuring all processes start at different times
time.sleep(randint(1,10))


for line in lines:
    #p = Process(target=abuse, args=(line.split(':::')[0],line.split(':::')[1]))
    #p.daemon = True
    #p.start()
    if verbose:
        asyncio.run(abuse(line.split(':::')[0],line.split(':::')[1]))
        counter += 1
    else:
        try:
            asyncio.run(asyncio.wait_for(abuse(line.split(':::')[0],line.split(':::')[1]), 300))
            counter += 1
        except:
            print('[Error] FAIL')
    print(f'[Success] {line.split(":::")[1][:-2]} is signing up on {line.split(":::")[0]}')
    print(f'[Status] {str(counter*config.processes)} accounts being cheated in')
    time_elapsed = time.time()-start
    try:
        time_per = time_elapsed/counter
    except:
        time_per = 25

    per_hour = 3600/time_per
    print(f'[Status] {round(time_per*100/config.processes)/100} seconds per scam / {round(per_hour*config.processes)} scams per hour')
    if counter == 100:
        counter = 10
        time_elapsed = time_elapsed/10
        start = time.time()-time_elapsed
