# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 16:00:23 2023

@author: skynet
"""

from faker import Faker
from random import randint
import json

fake = Faker()

def fakeemail(fname,lname):
    return f'{fname}{lname}{randint(1,999999)}@quackertonai.com'.lower()

emails = []

data = []


def savefakes():
    counter = 0
    for i in range(10_000):
        counter += 1
        print('[Status] ' + str(round(counter/10)/10) + '% done making fake data')
        fname = fake.first_name()
        lname = fake.last_name()
        done = False
        while not done:
            email = fakeemail(fname,lname)
            if not email in emails:
                done = True
        emails.append(email)
        data.append(f'{email}:::{fname} {lname}')
    
    counter = 0
    
    filename = 'fakedata/' + fake.first_name() + '.txt'
    
    with open(filename, 'w') as f:
        for datachunk in data:
            counter += 1
        #    print('[Status] ' + str(round(counter/10)/10) + '% done making fake data')
            f.write(datachunk)
            f.write('\n')
    return filename
