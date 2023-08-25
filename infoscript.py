#import config
import requests
import re

def getinfo(ref_link):
    r = requests.get(ref_link)
#    print('URL FOUND: ' + r.url)
    chunks = r.url.split('/')
    contid = re.sub('\D', '', chunks[3]).strip()
    refid = chunks[4].strip()
#    print(f'Contid: {contid}, Refid: {refid}')
    return [contid, refid]
