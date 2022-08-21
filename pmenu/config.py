import os
from pathlib import Path

PASSWORD_STORE_DIR = Path(os.environ.get("PASSWORD_STORE_DIR", "~/.password-store")).expanduser()
