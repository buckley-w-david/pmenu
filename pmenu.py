#!/home/david/Projects/pmenu/.venv/bin/python

import os, sys
import pathlib
import subprocess
import tldextract

from xdg import xdg_data_home

def fake_pass_base(true_base, url):
    ext = tldextract.extract(url)
    general_name = pathlib.Path(true_base, f'{ext.domain}.{ext.suffix}')
    sub_name = pathlib.Path(true_base, f'{ext.subdomain}.{ext.domain}.{ext.suffix}')

    if ext.subdomain and sub_name.is_dir():
        return str(sub_name)
    elif ext.subdomain and sub_name.is_file():
        return str(sub_name.parent)
    elif general_name.is_dir():
        return str(general_name)
    elif general_name.is_file():
        return str(general_name.parent)
    return true_base

try:
    with open(xdg_data_home() / 'TabFS/mnt/tabs/last-focused/url.txt', 'r') as f:
        url = f.read()
except:
    url = ''

os.environ['PASSWORD_STORE_DIR'] = str(fake_pass_base('/home/david/.password-store', url))
subprocess.run(['passmenu', *sys.argv[1:]], env=os.environ)
