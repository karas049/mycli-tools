import random

# 캐릭터 데이터
PLAYER = {"name": "용사", "hp": 100, "atk": 15, "def": 5}
ENEMIES = [
    {"name": "고블린", "hp": 50, "atk": 10, "def": 2},
    {"name": "늑대", "hp": 60, "atk": 12, "def": 3},
    {"name": "트롤", "hp": 100, "atk": 15, "def": 5},
]

def player_turn(player, enemy):
    """플레이어의 턴을 처리합니다."""
    print("\n[플레이어 턴]")
    print("[1] 공격  [2] 방어  [3] 회복")
    action = input(">> 행동을 선택하세요: ")
    if action == "1":
        damage = max(1, player["atk"] - enemy["def"])
        enemy["hp"] -= damage
        print(f"{player['name']}이(가) {enemy['name']}에게 {damage}의 피해를 입혔습니다! (적 HP: {enemy['hp']})")
    elif action == "2":
        player["def"] += 3
        print(f"{player['name']}이(가) 방어를 선택했습니다. (DEF +3)")
    elif action == "3":
        heal = random.randint(10, 20)
        player["hp"] += heal
        print(f"{player['name']}이(가) 회복을 선택했습니다. (HP +{heal})")
    else:
        print("잘못된 입력입니다. 턴을 넘깁니다.")

def enemy_turn(player, enemy):
    """적의 턴을 처리합니다."""
    print("\n[적 턴]")
    damage = max(1, enemy["atk"] - player["def"])
    player["hp"] -= damage
    print(f"{enemy['name']}이(가) {player['name']}에게 {damage}의 피해를 입혔습니다! (플레이어 HP: {player['hp']})")

def battle(player, enemy):
    """전투를 처리합니다."""
    print(f"\n⚔️ {enemy['name']}와(과) 전투를 시작합니다!")
    while player["hp"] > 0 and enemy["hp"] > 0:
        player_turn(player, enemy)
        if enemy["hp"] <= 0:
            print(f"\n🎉 {enemy['name']}을(를) 처치했습니다!")
            return True
        enemy_turn(player, enemy)
        if player["hp"] <= 0:
            print("\n💀 게임 오버! 플레이어가 쓰러졌습니다.")
            return False

def game_loop():
    """게임 루프를 처리합니다."""
    print("\n🕯️ 간단한 텍스트 RPG를 시작합니다!")
    for enemy in ENEMIES:
        if not battle(PLAYER, enemy):
            break
    else:
        print("\n🎯 모든 적을 처치했습니다! 게임 클리어!")

def simple_text_rpg_menu():
    """텍스트 RPG 메뉴를 출력하고 사용자 입력을 처리합니다."""
    while True:
        print("\n[텍스트 RPG 메뉴]")
        print("[1] 게임 시작")
        print("[b] 돌아가기")
        choice = input(">> 원하는 작업을 선택하세요: ")
        if choice == "1":
            game_loop()
        elif choice == "b":
            break
        else:
            print("잘못된 입력입니다. 다시 시도하세요.")
