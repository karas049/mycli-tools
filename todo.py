import json
import os
from datetime import datetime, timedelta
from tabulate import tabulate

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TODO_DIR = os.path.join(BASE_DIR, "data", "todo_lists")
DATE_FORMAT = "%Y-%m-%d"

current_todos = []

def get_todo_file(date=None):
    if date is None:
        date = datetime.now().strftime(DATE_FORMAT)
    return os.path.join(TODO_DIR, f"{date}.json")

def load_todos(date=None):
    """할 일 데이터를 로드합니다."""
    global current_todos
    todo_file = get_todo_file(date)
    ensure_directory_exists(os.path.dirname(todo_file))
    if not os.path.exists(todo_file):
        current_todos = []
    else:
        with open(todo_file, "r", encoding="utf-8") as file:
            current_todos = json.load(file)
    return current_todos

def ensure_directory_exists(directory):
    """디렉토리가 존재하지 않으면 생성합니다."""
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"디렉토리가 생성되었습니다: {os.path.abspath(directory)}")
    except Exception as e:
        print(f"디렉토리 생성 중 오류가 발생했습니다: {e}")

def save_todos(date=None):
    """현재 할 일 데이터를 JSON 파일로 저장합니다."""
    global current_todos
    todo_file = get_todo_file(date)
    ensure_directory_exists(os.path.dirname(todo_file))  # 디렉토리 생성 보장
    try:
        with open(todo_file, "w", encoding="utf-8") as file:
            json.dump(current_todos, file, ensure_ascii=False, indent=4)
        print(f"'{todo_file}'에 할 일이 저장되었습니다. (파일 경로: {os.path.abspath(todo_file)})")
    except Exception as e:
        print(f"할 일 저장 중 오류가 발생했습니다: {e}")

def display_todos(todos):
    """할 일을 표 형식으로 출력합니다."""
    if not todos:
        print("할 일이 없습니다.")
    else:
        table = [[idx + 1, "✔" if todo["done"] else "✘", todo["task"]] for idx, todo in enumerate(todos)]
        print(tabulate(table, headers=["번호", "상태", "할 일"], tablefmt="fancy_grid"))

def compare_with_yesterday():
    today = datetime.now().strftime(DATE_FORMAT)
    yesterday = (datetime.now() - timedelta(days=1)).strftime(DATE_FORMAT)

    today_todos = load_todos(today)
    yesterday_todos = load_todos(yesterday)

    print("\n[어제와 오늘의 Todo 리스트 비교]")
    print("어제:")
    display_todos(yesterday_todos)
    print("\n오늘:")
    display_todos(today_todos)

def add_todo():
    """새로운 할 일을 추가합니다."""
    global current_todos
    task = input("추가할 할 일을 입력하세요: ")
    current_todos.append({"task": task, "done": False})
    print(f"'{task}' 할 일이 추가되었습니다. 저장하려면 '저장하기'를 선택하세요.")

def delete_todo():
    """할 일을 삭제합니다."""
    global current_todos
    if not current_todos:
        print("삭제할 할 일이 없습니다.")
        return

    display_todos(current_todos)
    try:
        idx = int(input("삭제할 할 일 번호를 입력하세요: ")) - 1
        if 0 <= idx < len(current_todos):
            removed = current_todos.pop(idx)
            print(f"'{removed['task']}'가 삭제되었습니다. 저장하려면 '저장하기'를 선택하세요.")
        else:
            print("잘못된 번호입니다.")
    except ValueError:
        print("유효한 번호를 입력하세요.")

def toggle_todo():
    todos = load_todos()
    display_todos(todos)
    try:
        idx = int(input("완료 상태를 변경할 할 일 번호를 입력하세요: ")) - 1
        if 0 <= idx < len(todos):
            todos[idx]["done"] = not todos[idx]["done"]
            save_todos(todos)
            print(f"'{todos[idx]['task']}'의 상태가 변경되었습니다.")
        else:
            print("잘못된 번호입니다.")
    except ValueError:
        print("유효한 번호를 입력하세요.")

def todo_menu():
    """Todo 리스트 메뉴를 출력하고 사용자 입력을 처리합니다."""
    load_todos()  # 할 일 데이터를 로드
    while True:
        print("\n[Todo 리스트 메뉴]")
        print("[1] 할 일 보기")
        print("[2] 할 일 추가")
        print("[3] 할 일 삭제")
        print("[4] 완료 상태 변경")
        print("[5] 저장하기")  # 저장하기 항목 추가
        print("[b] 돌아가기")
        choice = input(">> 원하는 작업을 선택하세요: ")
        if choice == "1":
            display_todos(current_todos)
        elif choice == "2":
            add_todo()
        elif choice == "3":
            delete_todo()
        elif choice == "4":
            toggle_todo()
        elif choice == "5":
            save_todos()
        elif choice == "b":
            break
        else:
            print("잘못된 입력입니다. 다시 시도하세요.")
