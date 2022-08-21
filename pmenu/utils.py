import pathlib
import tldextract

from pmenu.config import PASSWORD_STORE_DIR


def fake_pass_base(url: str) -> str:
    ext = tldextract.extract(url)
    general_name = PASSWORD_STORE_DIR / f"{ext.domain}.{ext.suffix}"
    sub_name = PASSWORD_STORE_DIR / f"{ext.subdomain}.{ext.domain}.{ext.suffix}"

    if ext.subdomain and sub_name.is_dir():
        return str(sub_name)
    elif ext.subdomain and sub_name.is_file():
        return str(sub_name.parent)
    elif general_name.is_dir():
        return str(general_name)
    elif general_name.is_file():
        return str(general_name.parent)
    return str(PASSWORD_STORE_DIR)
