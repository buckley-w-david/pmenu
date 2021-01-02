#!/home/david/Projects/pmenu/.venv/bin/python

import os, sys
import pathlib
import subprocess
import tldextract

def fake_pass_base(true_base, url):
    ext = tldextract.extract(url)
    name = pathlib.Path(true_base, f'{ext.domain}.{ext.suffix}')
    if name.is_dir():
        return name
    elif name.is_file():
        return name.parent
    elif ext.subdomain:
        name = pathlib.Path(true_base, f'{ext.subdomain}.{ext.domain}.{ext.suffix}')
        if name.is_dir():
            return name
        elif name.is_file():
            return name.parent
    return true_base

try:
    with open('/home/david/Source/TabFS/fs/mnt/tabs/last-focused/url.txt', 'r') as f:
        url = f.read()
except:
    url = ''

os.environ['PASSWORD_STORE_DIR'] = str(fake_pass_base('/home/david/.password-store', url))
subprocess.run(['passmenu', *sys.argv[1:]], env=os.environ)
