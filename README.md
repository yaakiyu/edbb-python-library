# edbb-python-library
EDBBのPythonライブラリ実装。

## 概要
- dependenciesにdiscord.pyやdotenvを含むことでpip installの手間を軽減する
- バージョンチェック (古いコードだったりすると動作しない旨をエラー表示する)
- エラー時にEDBBに関する情報と公式サポートへの案内を表示

## How to build and publish?
(参考： https://qiita.com/c60evaporator/items/e1ecccab07a607487dcf )
```sh
# ビルド
python setup.py sdist
python setup.py bdist_wheel

# テスト環境
twine upload --repository testpypi dist/*
# 動作確認用
pip install --index-url https://test.pypi.org/simple/ edbb

# 本番環境へのアップロード
twine upload --repository pypi dist/*
```