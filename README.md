# Password Tool

Flaskで構築されたシンプルなパスワードチェッカーおよびパスワード生成ツールです。

このアプリケーションでは、以下の機能を利用できます：
- パスワードが漏洩していないかを確認する
- 安全なランダムパスワードを生成する

---

## Tech Stack

[Python]
[Flask]
[HTML]
[CSS]

---

## Features

- パスワード漏洩チェック機能
- ランダムパスワード生成機能
- 複数の文字種選択機能
- Flaskバックエンドとの連携

---

## What Users Can Do

### Password Checker
ユーザーは以下の操作が可能です：
- パスワードを入力する
- パスワードが漏洩していないか確認する
- 漏洩件数の結果を確認する

### Password Generator
ユーザーは以下の操作が可能です：
- 文字の種類を選択する
    - 小文字
    - 大文字
    - 数字
    - 記号
- パスワードの長さを選択する
- ランダムなパスワードを生成する

---

## Process Flow

### Password Checker

```text
User Input
    ↓
Flask Server
    ↓
SHA1 Password Hashing
    ↓
Pwned Password API
    ↓
Result Display
```

---

### Password Generator

```text
User Option Selection
    ↓
Flask Server
    ↓
Character Set Generation
    ↓
Random Password Generation
    ↓
Result Display
```

---

## Project Structure

```text
project/

├── server.py
├── checkmypass.py
├── create_password.py
│
├── templates/
│   ├── index.html
│   ├── check.html
│   └── create.html
│
└── static/
    └── style.css
```

## Run Application

```bash
python server.py
```

Open browser:

```text
https://password-tool-6l7p.onrender.com/
```

---

## Deploy

This project is deployed using Render.

---

## Learned

このプロジェクトを通じて、以下のことを学びました：
- Flaskのルーティング
- バックエンドとフロントエンドの連携
- API通信
- パスワードのハッシュ化
- レスポンシブWebデザイン
- Pythonのモジュール化

---

## Future Improvements

- パスワードコピーボタン
- パスワードの強度表示
- モバイルUIの改善
- UXデザインの向上

---

## Author

Tatsuya

---

## Video


https://github.com/user-attachments/assets/a25d4479-9092-445d-a77b-129192a9bf1f

