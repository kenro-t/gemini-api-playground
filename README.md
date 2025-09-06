# GEMINI API PLAYGROUND

ドキュメント  
https://ai.google.dev/gemini-api/docs/quickstart

## memo

#### genaiパッケージをインストール

`uv pip install -q -U google-genai`

#### 画像生成用のパッケージをインストール

`uv pip install Pillow`

#### uvで環境変数を利用して実行

`uv run --env-file .env -- python main.py`