import json
import os
import re
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MEMO_DIR = os.path.join(BASE_DIR, "data", "memo")
EXPORT_DIR = os.path.join(BASE_DIR, "data", "trans")
DATE_FORMAT = "%Y-%m-%d"

# 상수 정의
INVALID_NUMBER_MESSAGE = "잘못된 번호입니다."
ENTER_VALID_NUMBER_MESSAGE = "유효한 번호를 입력하세요."

# 전역 변수로 메모 데이터를 유지
current_notes = []

def ensure_directory_exists(directory):
    """디렉토리가 존재하지 않으면 생성합니다."""
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"디렉토리가 생성되었습니다: {directory}")
    except Exception as e:
        print(f"디렉토리 생성 중 오류가 발생했습니다: {e}")

def get_note_file(title):
    """메모 제목을 기반으로 JSON 파일 경로를 반환합니다."""
    sanitized_title = sanitize_filename(title)
    return os.path.join(MEMO_DIR, f"{sanitized_title}.json")

def load_notes():
    """memo 폴더에 저장된 모든 메모를 불러옵니다."""
    global current_notes
    ensure_directory_exists(MEMO_DIR)
    current_notes = []
    for filename in os.listdir(MEMO_DIR):
        if filename.endswith(".json"):
            with open(os.path.join(MEMO_DIR, filename), "r", encoding="utf-8") as file:
                current_notes.append(json.load(file))
    return current_notes

def save_notes():
    """현재 메모 데이터를 memo 폴더에 저장합니다."""
    ensure_directory_exists(MEMO_DIR)
    for note in current_notes:
        note_file = get_note_file(note["title"])
        try:
            with open(note_file, "w", encoding="utf-8") as file:
                json.dump(note, file, ensure_ascii=False, indent=4)
            print(f"'{note['title']}' 메모가 저장되었습니다. (파일 경로: {note_file})")
        except Exception as e:
            print(f"메모 저장 중 오류가 발생했습니다: {e}")

def display_page(notes, start_idx, end_idx, current_page):
    """현재 페이지의 메모를 출력합니다."""
    page_notes = notes[start_idx:end_idx]
    print(f"\n[메모 보기 - 페이지 {current_page + 1}]")
    for idx, note in enumerate(page_notes, start=start_idx + 1):
        print(f"{idx}. [{note['date']}] {note['title']}")

def handle_page_navigation(notes, current_page, page_size):
    """페이지 이동을 처리합니다."""
    total_pages = (len(notes) + page_size - 1) // page_size
    if current_page < 0:
        print("이전 페이지가 없습니다.")
        return 0
    elif current_page >= total_pages:
        print("다음 페이지가 없습니다.")
        return total_pages - 1
    return current_page

def view_note_detail(notes):
    """선택한 메모의 상세 내용을 출력합니다."""
    try:
        note_idx = int(input(">> 상세히 볼 메모 번호를 입력하세요: ")) - 1
        if 0 <= note_idx < len(notes):
            note = notes[note_idx]
            print("\n[메모 상세 보기]")
            print(f"작성 날짜: {note['date']}")
            print(f"제목: {note['title']}")
            print(f"내용:\n{note['content']}")
        else:
            print(INVALID_NUMBER_MESSAGE)
    except ValueError:
        print(ENTER_VALID_NUMBER_MESSAGE)

def list_notes_paginated():
    """메모를 5개씩 페이지로 나누어 출력하고 상세 보기 기능을 제공합니다."""
    notes = load_notes()
    if not notes:
        print("저장된 메모가 없습니다.")
        return

    page_size = 5
    current_page = 0

    while True:
        start_idx = current_page * page_size
        end_idx = start_idx + page_size
        display_page(notes, start_idx, end_idx, current_page)

        print("\n[n] 다음 페이지")
        print("[p] 이전 페이지")
        print("[v] 메모 보기")
        print("[b] 돌아가기")
        choice = input(">> 원하는 작업을 선택하세요: ")

        if choice == "n":
            current_page = handle_page_navigation(notes, current_page + 1, page_size)
        elif choice == "p":
            current_page = handle_page_navigation(notes, current_page - 1, page_size)
        elif choice == "v":
            view_note_detail(notes)
        elif choice == "b":
            break
        else:
            print("잘못된 입력입니다. 다시 시도하세요.")

def add_note():
    """새로운 메모를 추가합니다."""
    global current_notes
    title = input("메모 제목을 입력하세요: ")
    content = input("메모 내용을 입력하세요: ")
    current_notes.append({
        "date": datetime.now().strftime(DATE_FORMAT),
        "title": title,
        "content": content
    })
    print(f"'{title}' 메모가 추가되었습니다. 저장하려면 '저장하기'를 선택하세요.")

def sanitize_filename(filename):
    """파일 이름에서 유효하지 않은 문자를 제거합니다."""
    return re.sub(r'[\\/*?:"<>|]', '_', filename)

def export_notes():
    """memo 폴더에서 선택한 메모를 trans 폴더로 내보냅니다."""
    notes = load_notes()
    if not notes:
        print("내보낼 메모가 없습니다.")
        return
    ensure_directory_exists(EXPORT_DIR)
    for note in notes:
        sanitized_title = sanitize_filename(note['title'])
        export_file = os.path.join(EXPORT_DIR, f"{note['date']}_{sanitized_title}.txt")
        try:
            with open(export_file, "w", encoding="utf-8") as file:
                file.write(f"제목: {note['title']}\n")
                file.write(f"날짜: {note['date']}\n")
                file.write(f"내용:\n{note['content']}\n")
            print(f"'{note['title']}' 메모가 '{EXPORT_DIR}' 디렉토리로 내보내졌습니다. (파일 경로: {export_file})")
        except Exception as e:
            print(f"메모 내보내기 중 오류가 발생했습니다: {e}")

def delete_note():
    """메모를 삭제합니다."""
    global current_notes
    if not current_notes:
        print("삭제할 메모가 없습니다.")
        return

    print("\n[삭제할 메모 목록]")
    for idx, note in enumerate(current_notes, start=1):
        print(f"{idx}. [{note['date']}] {note['title']}")

    try:
        idx = int(input("삭제할 메모 번호를 입력하세요: ")) - 1
        if 0 <= idx < len(current_notes):
            removed_note = current_notes.pop(idx)
            print(f"'{removed_note['title']}' 메모가 삭제되었습니다. 저장하려면 '저장하기'를 선택하세요.")
        else:
            print(INVALID_NUMBER_MESSAGE)
    except ValueError:
        print(ENTER_VALID_NUMBER_MESSAGE)

def notepad_menu():
    """메모장 메뉴를 출력하고 사용자 입력을 처리합니다."""
    load_notes()  # 메모 데이터를 로드
    while True:
        print("\n[메모장 메뉴]")
        print("[1] 메모 보기")
        print("[2] 메모 추가")
        print("[3] 메모 삭제")
        print("[4] 메모 내보내기")
        print("[5] 저장하기")  # 저장하기 항목 추가
        print("[b] 돌아가기")
        choice = input(">> 원하는 작업을 선택하세요: ")
        if choice == "1":
            for idx, note in enumerate(current_notes, start=1):
                print(f"{idx}. [{note['date']}] {note['title']}")
        elif choice == "2":
            add_note()
        elif choice == "3":
            delete_note()
        elif choice == "4":
            export_notes()
        elif choice == "5":
            save_notes()
        elif choice == "b":
            break
        else:
            print(repr("잘못된 입력입니다. 다시 시도하세요."))
