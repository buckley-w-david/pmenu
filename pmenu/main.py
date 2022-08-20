#!/home/david/.cache/pypoetry/virtualenvs/pmenu-CQJe8C2t-py3.10/bin/python

import os, sys, json, struct
import pathlib
import subprocess
import tldextract

from xdg import xdg_data_home

from pmenu import mozlz4a

PASSWORD_STORE_DIR = '/home/david/.password-store'

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

def main():
    with open('/home/david/.mozilla/firefox/jvuf14a2.default-release/sessionstore-backups/recovery.jsonlz4', 'rb') as f:
        data = json.loads(mozlz4a.decompress(f))

    window = data["selectedWindow"]-1
    tab = data["windows"][window]["selected"]-1
    url = data["windows"][window]["tabs"][tab]['entries'][-1]["url"]

    os.environ['PASSWORD_STORE_DIR'] = fake_pass_base(url)
    subprocess.run(['passmenu', *sys.argv[1:]], env=os.environ)
