# 🧰 MyCLI Tools

다기능 터미널 기반 유틸리티 도구 모음입니다.  
생산성과 재미를 동시에 추구하며, 한국어와 영어를 모두 지원합니다.  
할 일 관리, 메모장, 계산기, 타이머, 타자 연습, 텍스트 RPG, 타로 카드 등 다양한 기능이 포함되어 있습니다.

---

## 📦 기능 소개 (Features)

### 🛠️ 생산성 / 도구 (Productivity / Tools)

#### ✅ Todo 리스트
- 날짜별 JSON 파일로 관리되는 할 일 목록
- 할 일 추가, 삭제, 상태 변경, 저장 가능
- 어제와 오늘의 할 일 비교 기능 (`compare_with_yesterday`)
- 데이터 경로: `data/todo_lists/YYYY-MM-DD.json`

#### 📝 메모장
- 메모 추가, 삭제, 보기, 저장, 내보내기 기능 제공
- 5개씩 페이지 단위로 목록을 나눠서 보기 가능
- 각각의 메모는 `data/memo/제목.json`에 저장됨
- `.txt`로 내보내는 기능은 `data/trans/` 디렉토리를 사용
- 파일명은 자동으로 안전하게 정제됨 (`sanitize_filename()`)

#### 🧮 계산기
- **기본 연산**: 문자열 수식 입력 (`2 + 3 * 4`)
- **고급 연산**: 제곱근, 거듭제곱, 로그, 삼각함수 등 지원
- 수학 함수는 `math` 모듈 기반으로 처리됨

#### ⏰ 타이머 / 알림
- 초 단위 타이머 또는 시각 기반 알람 설정 가능
- 진행률 게이지바 및 남은 시간 실시간 표시
- 완료 시 별도의 터미널 창에서 메시지를 띄움 (`completion_script.py` 자동 생성)
- 예시 보조 스크립트: `timer_script.py`

#### 🗑️ JSON 휴지통
- `data/` 디렉토리 내 모든 `.json` 파일을 탐색하여 휴지통으로 이동
- `data/trash/` 폴더로 파일을 이동시켜 실제 삭제 없이 정리
- 향후 복구 기능 확장 가능

---

### 🎮 재미 / 창의 / 게임 (Fun / Creativity / Games)

#### 🔤 타자 연습
- 지원 언어: 영어, 독일어, 인도네시아어, 이탈리아어, 일본어
- 2단계 연습:
  1. 외국어 문장 입력
  2. 해당 문장의 한글 의미 입력
- 정확도 및 입력 시간 측정
- 연습 문장 출처: [Tatoeba 프로젝트](https://tatoeba.org/ko)
- 데이터 위치: `data/sentence/*.json`

#### ⚔️ 간단한 텍스트 RPG
- 플레이어와 적이 번갈아 공격하는 턴제 전투
- 3명의 적과 연속 전투:
  - 고블린, 늑대, 트롤
- 행동 선택: 공격 / 방어 / 회복
- 승리 시 다음 적과 전투, HP가 0이 되면 게임 오버

#### 🔮 오늘의 타로
- 22장의 메이저 아르카나 카드 중 3장을 무작위 추출
- 카드 이름과 키워드를 `rich` 테이블로 출력
- 예시: `The Star` → 희망, 영감, 치유
- ⚠️ 현재 `"The Hierophant"` 카드가 중복으로 2회 등록되어 있음

---

## 🌐 다국어 지원 (Language Support)

- [3] 메뉴에서 한국어/영어 전환 가능
- 모든 메시지는 다국어 `MESSAGES` 딕셔너리를 통해 관리됨

> ⚠️ **언어 전환 기능은 메인 메뉴에서만 적용됩니다.**  
> 전체 메뉴에서의 다국어 적용은 구조적 문제로 인해 이번 프로젝트에서는 포기하였습니다.  
> **다음 프로젝트에서는 초기 설계 단계부터 다국어 지원을 고려할 예정입니다.**

---

### 실행 (Windows EXE 버전) 
이 프로젝트는 **PyInstaller**를 사용하여 `.exe` 파일로 빌드하여 Python 없이 바로 실행 가능합니다. 
---

실행 시 메인 메뉴가 출력됩니다:

```
==============================
       🧰 MyCLI Tools       
==============================
[1] 생산성 / 도구
[2] 재미 / 창의 / 게임
[3] 언어
[0] 종료
>> 원하는 메뉴를 입력하세요:
```

---

## 📁 프로젝트 구조 (Structure)

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
│   │       └── completion_script.py (자동 생성)
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

## 📜 라이선스 (License)

MIT License  
본 프로젝트는 누구나 자유롭게 사용, 복사, 수정, 병합, 게시, 배포, 재라이선스, 판매할 수 있습니다.  
보다 자유로운 오픈소스 생태계를 지향합니다.

---

## 🗣️ 언어 지원에 대한 고지 (Language Support Notice)

### 🇰🇷 한국어  
현재 언어 전환 기능은 메인 메뉴에서만 적용되며, 전체 메뉴의 다국어화는 구조상 어려움으로 이번 프로젝트에선 포기했습니다.  
다음에는 처음부터 다국어 지원을 고려하여 설계할 계획입니다.

### 🇺🇸 English  
Language switching is available **only in the main menu**.  
Full multilingual support was considered but later abandoned due to structural limitations.  
It will be properly planned from the beginning in future projects.

### 🇯🇵 日本語  
言語の切り替えは**メインメニューのみ**対応しています。  
全体の多言語対応は構造上の都合により今回は見送られました。  
次回は設計段階から多言語対応を考慮します。
