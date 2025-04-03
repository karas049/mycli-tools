import random
from rich.console import Console
from rich.table import Table

console = Console()

# 아르카나 카드 데이터
TAROT_CARDS = [
    {"name": "The Fool", "keyword": "새로운 시작, 자유, 모험"},
    {"name": "The Magician", "keyword": "창조성, 잠재력, 기술"},
    {"name": "The High Priestess", "keyword": "직관, 신비, 내면의 지혜"},
    {"name": "The Empress", "keyword": "풍요, 창조성, 자연"},
    {"name": "The Emperor", "keyword": "권위, 안정, 구조"},
    {"name": "The Hierophant", "keyword": "전통, 지혜, 영적 지도"},
    {"name": "The Lovers", "keyword": "사랑, 조화, 관계"},
    {"name": "The Chariot", "keyword": "의지, 승리, 전진"},
    {"name": "Strength", "keyword": "용기, 인내, 내면의 힘"},
    {"name": "The Hermit", "keyword": "고독, 성찰, 내면의 탐구"},
    {"name": "Wheel of Fortune", "keyword": "운명, 변화, 행운"},
    {"name": "Justice", "keyword": "공정, 진실, 책임"},
    {"name": "The Hanged Man", "keyword": "희생, 새로운 관점, 멈춤"},
    {"name": "Death", "keyword": "변화, 끝, 새로운 시작"},
    {"name": "Temperance", "keyword": "균형, 조화, 절제"},
    {"name": "The Devil", "keyword": "유혹, 속박, 그림자"},
    {"name": "The Tower", "keyword": "혼란, 붕괴, 해방"},
    {"name": "The Star", "keyword": "희망, 영감, 치유"},
    {"name": "The Moon", "keyword": "환상, 직관, 불확실성"},
    {"name": "The Sun", "keyword": "행복, 성공, 긍정"},
    {"name": "Judgement", "keyword": "부활, 평가, 깨달음"},
    {"name": "The World", "keyword": "완성, 성취, 통합"},
    {"name": "The Hierophant", "keyword": "전통, 지혜, 영적 지도"}
]

def draw_tarot():
    """타로 카드 3장을 랜덤으로 뽑아 키워드를 출력합니다."""
    console.print("\n🔮 [bold magenta]오늘의 타로 카드[/bold magenta] 🔮", style="bold magenta")
    selected_cards = random.sample(TAROT_CARDS, 3)

    table = Table(title="오늘의 타로 카드")
    table.add_column("번호", justify="center", style="cyan", no_wrap=True)
    table.add_column("카드 이름", justify="center", style="green")
    table.add_column("키워드", justify="center", style="yellow")

    for idx, card in enumerate(selected_cards, start=1):
        table.add_row(str(idx), card["name"], card["keyword"])

    console.print(table)

def tarot_menu():
    """오늘의 타로 메뉴를 출력하고 사용자 입력을 처리합니다."""
    while True:
        print("\n[오늘의 타로 메뉴]")
        print("[1] 타로 카드 뽑기")
        print("[b] 돌아가기")
        choice = input(">> 원하는 작업을 선택하세요: ")
        if choice == "1":
            draw_tarot()
        elif choice == "b":
            break
        else:
            print("잘못된 입력입니다. 다시 시도하세요.")
