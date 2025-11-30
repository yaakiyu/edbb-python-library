import dotenv
dotenv.load_dotenv()


import sys
from .l10n import get_text


__version__ = "0.2.0"


# Pythonのバージョンを確認
if sys.version_info[1] < 8:
    print(get_text("python_version_error"))
    exit(1)


# discord.pyのバージョンを確認 (このパッケージをインストールした時点でdiscord.pyがインストールされているはず)
import discord
import urllib.request
import json
import traceback


if discord.__version__[0] < "2":
    print(get_text("discord_py_version_error"))
    exit(1)


def get_latest_pypi_version_urllib(package_name):
    url = f"https://pypi.org/pypi/{package_name}/json"
    try:
        with urllib.request.urlopen(url) as response:
            if response.status == 200:
                data = response.read()
                package_info = json.loads(data)
                return package_info["info"]["version"]
    except Exception:
        print(get_text("warning_fetching_version"))
        traceback.print_exc()
    return None


latest_version = get_latest_pypi_version_urllib("edbb")
if latest_version is not None and latest_version != __version__:
    print(get_text("new_version_available"))
