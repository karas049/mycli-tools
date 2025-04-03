import sys
import os
from colorama import Fore, Style, init
init(autoreset=True)

# 프로젝트 루트 디렉토리를 Python 경로에 추가
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.append(PROJECT_ROOT)

from tools.productivity.todo import todo_menu
from tools.productivity.notepad import notepad_menu
from tools.productivity.trash import trash_menu
from tools.productivity.calculator import calculator_menu
from tools.productivity.timer import timer_menu
from tools.fun.typing_practice import typing_practice_menu  # 타자 연습 메뉴 호출
from tools.fun.simple_text_rpg import simple_text_rpg_menu  # 간단한 텍스트 RPG 메뉴 호출
from tools.fun.tarot import tarot_menu  # 오늘의 타로 메뉴 호출

# 상수 정의
PROMPT_MESSAGE = ">> 원하는 메뉴를 입력하세요: "
BACK_OPTION = "[b] 돌아가기"

# 전역 변수로 언어 설정
LANGUAGE = "ko"  # 기본 언어는 한국어

# 다국어 메시지 정의
MESSAGES = {
    "ko": {
        "main_menu_title": "🧰 MyCLI Tools",
        "main_menu_options": ["[1] 생산성 / 도구", "[2] 재미 / 창의 / 게임", "[3] 언어", "[0] 종료"],
        "prompt_message": ">> 원하는 메뉴를 입력하세요: ",
        "back_option": "[b] 돌아가기",
        "invalid_input": "잘못된 입력입니다. 다시 시도하세요.",
        "exit_message": "프로그램을 종료합니다."
    },
    "en": {
        "main_menu_title": "🧰 MyCLI Tools",
        "main_menu_options": ["[1] Productivity / Tools", "[2] Fun / Creativity / Games", "[3] Language", "[0] Exit"],
        "prompt_message": ">> Please select an option: ",
        "back_option": "[b] Go back",
        "invalid_input": "Invalid input. Please try again.",
        "exit_message": "Exiting the program."
    }
}

def get_message(key):
    """현재 언어에 맞는 메시지를 반환합니다."""
    return MESSAGES[LANGUAGE][key]

def main_menu():
    print(f"{Fore.CYAN}==============================")
    print(f"{Fore.YELLOW}       {get_message('main_menu_title')}       ")
    print(f"{Fore.CYAN}==============================")
    for option in get_message("main_menu_options"):
        print(f"{Fore.GREEN}{option}")
    return input(get_message("prompt_message"))

def productivity_menu():
    print(f"{Fore.GREEN}[1-1] Todo 리스트")
    print(f"{Fore.GREEN}[1-2] 메모장")
    print(f"{Fore.GREEN}[1-3] 계산기")
    print(f"{Fore.GREEN}[1-4] 타이머/알림")
    print(f"{Fore.GREEN}[1-5] JSON 파일 휴지통으로 보내기")
    print(f"{Fore.YELLOW}{get_message('back_option')}")
    return input(get_message("prompt_message"))

def fun_menu():
    print(f"{Fore.GREEN}[2-1] 타자 연습")
    print(f"{Fore.GREEN}[2-2] 간단한 텍스트 RPG")
    print(f"{Fore.GREEN}[2-3] 오늘의 타로")
    print(f"{Fore.YELLOW}{get_message('back_option')}")
    return input(get_message("prompt_message"))

def language_menu():
    """언어 설정 메뉴를 출력하고 사용자 입력을 처리합니다."""
    global LANGUAGE
    while True:
        print("\n[언어 설정 / Language Settings]")
        print("[1] 한국어 (Korean)")
        print("[2] English")
        print(get_message("back_option"))
        choice = input(get_message("prompt_message"))
        if choice == "1":
            LANGUAGE = "ko"
            print("언어가 한국어로 설정되었습니다.")
        elif choice == "2":
            LANGUAGE = "en"
            print("Language has been set to English.")
        elif choice == "b":
            break
        else:
            print(get_message("invalid_input"))

def handle_sub_menu(menu_function):
    while True:
        sub_choice = menu_function()
        if sub_choice == "b":
            break
        elif sub_choice == "1-1":
            todo_menu()
        elif sub_choice == "1-2":
            notepad_menu()
        elif sub_choice == "1-3":
            calculator_menu()
        elif sub_choice == "1-4":
            timer_menu()
        elif sub_choice == "1-5":
            trash_menu()
        elif sub_choice == "2-1":
            typing_practice_menu()  # 타자 연습 메뉴 호출
        elif sub_choice == "2-2":
            simple_text_rpg_menu()  # 간단한 텍스트 RPG 메뉴 호출
        elif sub_choice == "2-3":
            tarot_menu()  # 오늘의 타로 메뉴 호출
        else:
            print(get_message("invalid_input"))

def main():
    while True:
        choice = main_menu()
        if choice == "0":
            print(get_message("exit_message"))
            sys.exit()
        elif choice == "1":
            handle_sub_menu(productivity_menu)
        elif choice == "2":
            handle_sub_menu(fun_menu)
        elif choice == "3":
            language_menu()
        else:
            print(get_message("invalid_input"))

if __name__ == "__main__":
    main()
