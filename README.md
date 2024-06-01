# FastAPI Document Check

このプロジェクトは、FastAPI を使用して開発されたドキュメントチェックアプリです。ユーザーはこのアプリを通じて、文書をアップロードし、指定された確認観点に基づいてその内容をチェックすることができます。

## 特徴

- 複数の文書形式のアップロードと処理サポート。
- ユーザーが指定する確認観点に基づく内容の確認。
- 簡潔で使いやすいフロントエンド。

## 技術スタック

- **FastAPI**: 高速で、現代的なWebアプリケーションを構築するためのPythonフレームワーク。
- **HTML/CSS**: ユーザーインターフェースの構築。
- **JavaScript**: フロントエンドの動的なインタラクションを実現。

## 開発環境の設定

プロジェクトをローカルで実行するには、以下の手順を実行してください。

### 前提条件

- Python 3.8 以上
- pip

### インストール手順

1. リポジトリをクローンします:

    ```bash
    git clone https://github.com/toku-dango/fastapi_document_check.git
    ```

2. 必要なパッケージをインストールします:

    ```bash
    cd fastapi_document_check
    pip install -r requirements.txt
    ```

3. アプリケーションを起動します:

    ```bash
    uvicorn main:app --reload
    ```

アプリケーションは `http://localhost:8000` でアクセスできます。

## 使用方法

- ブラウザで `http://localhost:8000` を開きます。
- ページの指示に従ってドキュメントをアップロードし、確認観点を入力します。
- 「送信」ボタンをクリックして、文書を送信します。

## ライセンス

このプロジェクトは [MIT license](LICENSE) の下で公開されています。
