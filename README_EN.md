# 🧰 MyCLI Tools

A multifunctional terminal-based utility suite for productivity and fun.  
Supports both Korean and English.  
Includes various tools like Todo list, Notepad, Calculator, Timer, Typing Practice, Text RPG, and Tarot Cards.

---

## 📦 Features

### 🛠️ Productivity / Tools

#### ✅ Todo List
- Manage todos in daily JSON files
- Add, delete, toggle status, and save todos
- Compare today’s and yesterday’s todos (`compare_with_yesterday`)
- Data path: `data/todo_lists/YYYY-MM-DD.json`

#### 📝 Notepad
- Add, delete, view, save, and export notes
- Notes are paginated (5 per page)
- Saved as `data/memo/title.json`
- Can be exported as `.txt` into `data/trans/`
- Filenames are automatically sanitized (`sanitize_filename()`)

#### 🧮 Calculator
- **Basic**: Evaluate math expressions (`2 + 3 * 4`)
- **Advanced**: Square root, powers, logs, trigonometry
- Uses Python's built-in `math` module

#### ⏰ Timer / Alarm
- Set countdown timer or alarm by clock time
- Shows real-time progress bar or remaining time
- Triggers notification in a new terminal window (`completion_script.py`)
- Includes standalone example: `timer_script.py`

#### 🗑️ JSON Trash
- Moves `.json` files in `data/` into `data/trash/`
- Files are not deleted, just moved
- Ideal for safe cleanup, potential recovery supported later

---

### 🎮 Fun / Creativity / Games

#### 🔤 Typing Practice
- Supported languages: English, German, Indonesian, Italian, Japanese
- Two-phase practice:
  1. Type foreign sentence
  2. Type Korean meaning
- Measures accuracy and time
- Sentence source: [Tatoeba Project](https://tatoeba.org/eng)
- Data files in: `data/sentence/*.json`

#### ⚔️ Simple Text RPG
- Turn-based combat between player and enemies
- Three enemies in sequence:
  - Goblin, Wolf, Troll
- Actions: Attack / Defend / Heal
- Defeat all to win, reach 0 HP to lose

#### 🔮 Daily Tarot
- Randomly draw 3 cards from 22 major arcana
- Displayed in colorful `rich` table
- Example: `The Star` → Hope, Inspiration, Healing
- ⚠️ `"The Hierophant"` appears twice due to duplication

---

## 🌐 Language Support

- Switch between Korean and English in menu option [3]
- All messages managed using a multilingual `MESSAGES` dictionary

> ⚠️ **Language switching only applies to the main menu.**  
> Full multilingual support was dropped due to structural limitations.  
> **Future projects will consider multi-language support from the start.**

---

### Execution (Windows EXE version)
This project is built using **PyInstaller** as a `.exe` file.  
It runs without requiring Python.

```bash
pyinstaller --noconfirm --onefile main.py
```

---

Main menu on launch:

```
==============================
       🧰 MyCLI Tools       
==============================
[1] Productivity / Tools
[2] Fun / Creativity / Games
[3] Language
[0] Exit
>> Enter your choice:
```

---

## 📁 Project Structure

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

## 📜 License

MIT License  
You are free to use, copy, modify, merge, publish, distribute, sublicense, and/or sell this software.

---

## 🗣️ Language Support Notice

### 🇰🇷 Korean  
언어 전환 기능은 메인 메뉴에서만 적용되며, 전체 다국어 지원은 이번 프로젝트에서는 제외되었습니다.  
다음 프로젝트에서는 초기 설계 단계부터 다국어 지원을 고려할 예정입니다.

### 🇺🇸 English  
Language switching is available **only in the main menu**.  
Full multilingual support was considered but later abandoned due to structural limitations.  
It will be properly planned from the beginning in future projects.

### 🇯🇵 Japanese  
言語の切り替えは**メインメニューのみ**対応しています。  
全体の多言語対応は構造上の都合により今回は見送られました。  
次回は設計段階から多言語対応を考慮します。
