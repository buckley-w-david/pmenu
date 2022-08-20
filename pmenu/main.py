import os, sys, json
import subprocess

from pmenu import mozlz4a, utils
from pmenu.config import FIREFOX_PROFILE_DIR

def main():
    with open(FIREFOX_PROFILE_DIR / "sessionstore-backups/recovery.jsonlz4", "rb") as f:
        data = json.loads(mozlz4a.decompress(f))

    window = data["selectedWindow"]-1
    tab = data["windows"][window]["selected"]-1
    url = data["windows"][window]["tabs"][tab]['entries'][-1]["url"]

    os.environ['PASSWORD_STORE_DIR'] = utils.fake_pass_base(url)
    subprocess.run(['passmenu', *sys.argv[1:]], env=os.environ)
