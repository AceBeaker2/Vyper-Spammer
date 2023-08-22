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
    vyperapi.get(link)

import fakeinfo

counter = 1

fakedata = fakeinfo.savefakes()

print('[Status] Fakes stored in ' + fakedata)

with open(fakedata, "r") as f:
    lines = f.readlines()

start = time.time()

# To stop network spam by ensuring all processes start at different times
time.sleep(randint(1,20))

import config

for line in lines:
    #p = Process(target=abuse, args=(line.split(':::')[0],line.split(':::')[1]))
    #p.daemon = True
    #p.start()
    asyncio.run(asyncio.wait_for(abuse(line.split(':::')[0],line.split(':::')[1]), 30))
    counter += 1
    print(f'[Success] {line.split(":::")[1][:-2]} is signing up on {line.split(":::")[0]}')
    print(f'[Status] {str(counter*config.processes)} accounts being cheated in')
    time_elapsed = time.time()-start
    time_per = time_elapsed/counter
    per_hour = 3600/time_per
    print(f'[Status] {round(time_per*100/config.processes)/100} seconds per scam / {round(per_hour*config.processes)} scams per hour')
