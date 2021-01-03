#!/home/david/Projects/pmenu/.venv/bin/python

import os, sys
import pathlib
import subprocess
import tldextract

from xdg import xdg_data_home

PASSWORD_STORE_DIR = '/home/david/.password-store'
LAST_URL_PATH = xdg_data_home() / 'TabFS/tabs/last-focused/url.txt'

def fake_pass_base(url: str) -> str:
    ext = tldextract.extract(url)
    general_name = pathlib.Path(PASSWORD_STORE_DIR, f'{ext.domain}.{ext.suffix}')
    sub_name = pathlib.Path(PASSWORD_STORE_DIR, f'{ext.subdomain}.{ext.domain}.{ext.suffix}')

    if ext.subdomain and sub_name.is_dir():
        return str(sub_name)
    elif ext.subdomain and sub_name.is_file():
        return str(sub_name.parent)
    elif general_name.is_dir():
        return str(general_name)
    elif general_name.is_file():
        return str(general_name.parent)
    return PASSWORD_STORE_DIR

try:
    with open(LAST_URL_PATH, 'r') as f:
        url = f.read()
except:
    url = ''

os.environ['PASSWORD_STORE_DIR'] = fake_pass_base(url)
subprocess.run(['passmenu', *sys.argv[1:]], env=os.environ)
