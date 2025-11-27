# 使用言語を推定、デフォルトは日本語
from typing import Optional
import locale
import os


SUPPORTED_LANGUAGES = ["ja_JP", "en_US"]

language = locale.getlocale()[0]

if language not in SUPPORTED_LANGUAGES:
    if os.getenv("EDBB_LANG") in SUPPORTED_LANGUAGES:
        language = os.getenv("EDBB_LANG")
    else:
        language = "ja_JP"
        print("[Warning] Unsupported locale detected. Defaulting to Japanese (ja_JP). To use English, please set your system locale to en_US.")


if language == "en_US":
    print("[Warning] This library has a partial English translation. Some messages may still appear in Japanese.")


# 文字列データ
STRING_DATA = {
    "python_version_error": {
        "ja_JP": "[エラー] このプログラムを起動するにはPython 3.8以降が必要です。Pythonのバージョンを確認してください。",
        "en_US": "[Error] This program requires Python 3.8 or higher to run. Please check your Python version.",
    },
    "discord_py_version_error": {
        "ja_JP": "[エラー] このプログラムを起動するにはdiscord.pyのバージョン2.0以降が必要です。discord.pyのバージョンを確認してください。",
        "en_US": "[Error] This program requires discord.py version 2.0 or higher to run. Please check your discord.py version.",
    },
    "new_version_available": {
        "ja_JP": "[情報] 新しいバージョンのedbbライブラリが利用可能です。`python -m pip install --upgrade edbb`でアップデートしてください。",
        "en_US": "[Info] A new version of the edbb library is available. Please update it using `pip install --upgrade edbb`.",
    },
    "warning_fetching_version": {
        "ja_JP": "[警告] EDBBライブラリの最新バージョンの情報を取得できませんでした。",
        "en_US": "[Warning] Could not fetch the latest version from PyPI.",
    },
    "error_message": {
        "ja_JP": "[エラー] botの起動中に上記の問題が発生しました。EDBBのドキュメントを参照してください。\nこの問題が解決できない場合は、公式サイト( https://himais0giiiin.com/ )よりdiscordサーバーに参加してサポートを受けてください。",
        "en_US": "[Error] An issue occurred while starting the bot. Please refer to the EDBB documentation.\nIf you cannot resolve this issue, please join the official Discord server for support ( https://himais0giiiin.com/ ).",
    },
}


def get_text(text_id: str, lang_code: Optional[str] = None) -> str:
    if lang_code is None:
        lang_code = language

    languages = STRING_DATA.get(text_id, {})
    return languages.get(lang_code, languages.get("ja_JP", "No message"))

