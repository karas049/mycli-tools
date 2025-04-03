# 🧰 MyCLI Tools

生産性と楽しさを提供する多機能なターミナルユーティリティです。  
韓国語と英語の切り替えに対応しています。  
Todoリスト、メモ帳、電卓、タイマー、タイピング練習、テキストRPG、タロットカードなどの機能が含まれています。

---

## 📦 機能紹介 (Features)

### 🛠️ 生産性 / ツール (Productivity / Tools)

#### ✅ Todoリスト
- 日別JSONファイルでタスクを管理
- タスクの追加・削除・状態変更・保存が可能
- 昨日との比較機能あり (`compare_with_yesterday`)
- データパス: `data/todo_lists/YYYY-MM-DD.json`

#### 📝 メモ帳
- メモの追加、削除、表示、保存、エクスポート機能
- ページ分けで5件ずつ表示
- メモは `data/memo/タイトル.json` に保存
- `.txt`として `data/trans/` にエクスポート可能
- ファイル名は安全な形式に自動変換 (`sanitize_filename()`)

#### 🧮 電卓
- **基本演算**: 数式文字列の入力 (`2 + 3 * 4`)
- **高度演算**: 平方根、累乗、対数、三角関数など
- Pythonの `math` モジュールを使用

#### ⏰ タイマー / アラーム
- 秒単位のタイマー、または時刻指定アラーム設定
- 進行状況バーや残り時間のリアルタイム表示
- 完了時は新しいターミナルで通知を表示 (`completion_script.py`)
- 補助スクリプト例: `timer_script.py`

#### 🗑️ JSON ゴミ箱
- `data/` 配下の `.json` ファイルを `data/trash/` に移動
- 削除せず安全に一時保存
- 将来的な復元機能の追加も可能

---

### 🎮 楽しみ / 創造性 / ゲーム

#### 🔤 タイピング練習
- 対応言語: 英語、ドイツ語、インドネシア語、イタリア語、日本語
- 二段階練習:
  1. 外国語の文をタイプ
  2. その意味を日本語で入力
- 正確度と入力時間を計測
- 文の出典: [Tatoebaプロジェクト](https://tatoeba.org/jpn)
- データ: `data/sentence/*.json`

#### ⚔️ 簡単なテキストRPG
- プレイヤーと敵によるターン制バトル
- 3体の敵と順番に戦闘:
  - ゴブリン、オオカミ、トロール
- 行動: 攻撃 / 防御 / 回復
- 全ての敵を倒せば勝利、HPが0になるとゲームオーバー

#### 🔮 本日のタロット
- 大アルカナ22枚の中から3枚をランダムで引く
- `rich` テーブルで名前とキーワードを表示
- 例: `The Star` → 希望、インスピレーション、癒し
- ⚠️ `"The Hierophant"` カードが重複して2回登録されている

---

## 🌐 言語サポート (Language Support)

- メニュー[3]で韓国語/英語を切り替え可能
- メッセージは多言語 `MESSAGES` 辞書で管理

> ⚠️ **言語切り替えはメインメニューのみに対応しています。**  
> 全体の多言語対応は構造上の制約により今回は断念しました。  
> **次回のプロジェクトでは最初から多言語対応を考慮して設計します。**

---

### 実行方法 (Windows EXE バージョン)
このプロジェクトは **PyInstaller** を使用して `.exe` ファイルにビルドされ、Pythonなしで実行可能です。

```bash
pyinstaller --noconfirm --onefile main.py
```

---

起動時に以下のメインメニューが表示されます:

```
==============================
       🧰 MyCLI Tools       
==============================
[1] 生産性 / ツール
[2] 楽しみ / 創造性 / ゲーム
[3] 言語
[0] 終了
>> 操作を選んでください:
```

---

## 📁 プロジェクト構成 (Structure)

```
MyCLI-Tools/
├── main.py
├── tools/
│   ├── productivity/
│   │   ├── todo.py
│   │   ├── notepad.py
│   │   ├── calculator.py
│   │   ├── timer.py
│   │   ├── trash.py
│   │   └── scripts/
│   │       └── completion_script.py
│   └── fun/
│       ├── typing_practice.py
│       ├── simple_text_rpg.py
│       └── tarot.py
├── data/
│   ├── memo/
│   ├── todo_lists/
│   ├── trans/
│   └── sentence/
└── requirements.txt
```

---

## 📜 ライセンス (License)

MITライセンス  
本プロジェクトは誰でも自由に使用、複製、改変、統合、公開、配布、サブライセンス、販売できます。

---

## 🗣️ 言語サポートに関するお知らせ (Language Support Notice)

### 🇰🇷 韓国語  
언어 전환 기능은 메인 메뉴에서만 적용되며, 전체 다국어 지원은 이번 프로젝트에서는 제외되었습니다.  
다음 프로젝트에서는 초기 설계 단계부터 다국어 지원을 고려할 예정입니다。

### 🇺🇸 英語  
Language switching is available **only in the main menu**.  
Full multilingual support was considered but later abandoned due to structural limitations.  
It will be properly planned from the beginning in future projects.

### 🇯🇵 日本語  
言語の切り替えは**メインメニューのみ**対応しています。  
全体の多言語対応は構造上の都合により今回は見送られました。  
次回は設計段階から多言語対応を考慮します。
