# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 10:09:56 2023

@author: skynet
"""

import requests
import infoscript

def send_api(email, name):
    headers = {
    'authority': 'vyper.io',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'accept-language': 'en-GB,en;q=0.5',
    'cache-control': 'max-age=0',
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryBrcOUq6BXlAM5KL3',
    'origin': 'https://vy.lc',
    'referer': 'https://vy.lc/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Brave";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-user': '?1',
    'sec-gpc': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
}
    contid, refid = infoscript.getinfo()

    params = {
    'contest_id': contid,
    'referrer_id': refid,
    'display_type': 'Landing Page',
    }

    data = f'------WebKitFormBoundaryBrcOUq6BXlAM5KL3\r\nContent-Disposition: form-data; name="_csrf"\r\n\r\nNVF1bFYtWVdmPSQ6ZxwwNl0zMlQTbxQ0czM2GhkaEBpdOhMEOhs/FA==\r\n------WebKitFormBoundaryBrcOUq6BXlAM5KL3\r\nContent-Disposition: form-data; name="Entries[contest_id]"\r\n\r\n442372\r\n------WebKitFormBoundaryBrcOUq6BXlAM5KL3\r\nContent-Disposition: form-data; name="Entries[referrer_id]"\r\n\r\n19096033\r\n------WebKitFormBoundaryBrcOUq6BXlAM5KL3\r\nContent-Disposition: form-data; name="Entries[registration_ip]"\r\n\r\n54.151.31.245\r\n------WebKitFormBoundaryBrcOUq6BXlAM5KL3\r\nContent-Disposition: form-data; name="Entries[gc]"\r\n\r\n1e213483\r\n------WebKitFormBoundaryBrcOUq6BXlAM5KL3\r\nContent-Disposition: form-data; name="Entries[full_name]"\r\n\r\n{name}\r\n------WebKitFormBoundaryBrcOUq6BXlAM5KL3\r\nContent-Disposition: form-data; name="Entries[email]"\r\n\r\n{email}\r\n------WebKitFormBoundaryBrcOUq6BXlAM5KL3\r\nContent-Disposition: form-data; name="terms_text"\r\n\r\non\r\n------WebKitFormBoundaryBrcOUq6BXlAM5KL3\r\nContent-Disposition: form-data; name="g-recaptcha-response"\r\n\r\n\r\n------WebKitFormBoundaryBrcOUq6BXlAM5KL3--\r\n'

    requests.post('https://vyper.io/entries/create', params=params, headers=headers, data=data)
    
def get(link):
    requests.get(link)
