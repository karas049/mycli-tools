import json
import os
import time
import random
from colorama import Fore, Style, init
init(autoreset=True)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_DIR = os.path.join(BASE_DIR, "data", "sentence")

LANGUAGE_FILES = {
    "1": {"file": "english_korean_sentences.json", "lang": "en"},
    "2": {"file": "german_korean_sentences.json", "lang": "de"},
    "3": {"file": "indonesian_korean_sentences.json", "lang": "id"},
    "4": {"file": "italian_korean_sentences.json", "lang": "it"},
    "5": {"file": "japanese_korean_sentences.json", "lang": "ja"}
}

def load_sentences(file_name):
    """JSON 파일에서 문장을 로드합니다."""
    file_path = os.path.join(DATA_DIR, file_name)
    if not os.path.exists(file_path):
        print(f"문장 파일을 찾을 수 없습니다: {file_path}")
        return []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError as e:
        print(f"JSON 파일 로드 중 오류가 발생했습니다: {e}")
        return []

def calculate_accuracy(original, typed):
    """사용자가 입력한 텍스트의 정확도를 계산합니다."""
    correct_chars = sum(1 for o, t in zip(original, typed) if o == t)
    return (correct_chars / len(original)) * 100 if original else 0

def typing_practice(sentences, lang):
    """타자 연습을 진행합니다."""
    if not sentences:
        print(f"{Fore.RED}문장이 없습니다. JSON 파일을 확인하세요.")
        return

    # 5문제를 랜덤으로 선택
    selected_sentences = random.sample(sentences, min(5, len(sentences)))

    for idx, sentence in enumerate(selected_sentences, start=1):
        print(f"\n{Fore.CYAN}[문제 {idx}]")
        print(f"{Fore.YELLOW}문장: {sentence[lang]}")
        print(f"{Fore.GREEN}의미: {sentence['ko']}")

        # 첫 번째 입력: 로마자 입력
        input(f"{Fore.MAGENTA}준비되셨으면 엔터를 눌러 시작하세요...")
        start_time = time.time()
        user_input = input(f"\n{Fore.BLUE}>> 로마자로 입력하세요: ")
        end_time = time.time()

        accuracy = calculate_accuracy(sentence[lang], user_input)
        elapsed_time = end_time - start_time
        print(f"{Fore.GREEN}정확도: {accuracy:.2f}%")
        print(f"{Fore.CYAN}입력 시간: {elapsed_time:.2f}초")

        # 두 번째 입력: 한글 입력
        input(f"{Fore.MAGENTA}준비되셨으면 엔터를 눌러 시작하세요...")
        start_time = time.time()
        user_input_ko = input(f"\n{Fore.BLUE}>> 이 문장의 의미를 한글로 입력하세요: ")
        end_time = time.time()

        accuracy_ko = calculate_accuracy(sentence["ko"], user_input_ko)
        elapsed_time_ko = end_time - start_time
        print(f"{Fore.GREEN}정확도: {accuracy_ko:.2f}%")
        print(f"{Fore.CYAN}입력 시간: {elapsed_time_ko:.2f}초")

def typing_practice_menu():
    """타자 연습 메뉴를 출력하고 사용자 입력을 처리합니다."""
    while True:
        print("\n[타자 연습 메뉴]")
        print("[1] 영어 - 한국어")
        print("[2] 독일어 - 한국어")
        print("[3] 인도네시아어 - 한국어")
        print("[4] 이탈리아어 - 한국어")
        print("[5] 일본어 - 한국어")
        print("[b] 돌아가기")
        choice = input(">> 원하는 언어를 선택하세요: ")

        if choice in LANGUAGE_FILES:
            file_info = LANGUAGE_FILES[choice]
            sentences = load_sentences(file_info["file"])
            typing_practice(sentences, file_info["lang"])
        elif choice == "b":
            break
        else:
            print("잘못된 입력입니다. 다시 시도하세요.")
