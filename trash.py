import os
import shutil

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_DIR = os.path.join(BASE_DIR, "data")
TRASH_DIR = os.path.join(DATA_DIR, "trash")

def ensure_directory_exists(directory):
    """디렉토리가 존재하지 않으면 생성합니다."""
    if not os.path.exists(directory):
        os.makedirs(directory)

def list_json_files():
    """data 하위 폴더에서 모든 JSON 파일을 나열합니다."""
    json_files = []
    for root, _, files in os.walk(DATA_DIR):
        if "trash" in root:
            continue  # 휴지통 폴더는 제외
        for file in files:
            if file.endswith(".json"):
                json_files.append(os.path.join(root, file))
    return json_files

def move_to_trash(file_path):
    """JSON 파일을 휴지통으로 이동합니다."""
    ensure_directory_exists(TRASH_DIR)
    try:
        file_name = os.path.basename(file_path)
        trash_path = os.path.join(TRASH_DIR, file_name)
        shutil.move(file_path, trash_path)
        print(f"'{file_path}'가 휴지통으로 이동되었습니다.")
    except Exception as e:
        print(f"파일 이동 중 오류가 발생했습니다: {e}")

def trash_menu():
    """휴지통으로 보낼 JSON 파일을 선택합니다."""
    json_files = list_json_files()
    if not json_files:
        print("휴지통으로 보낼 JSON 파일이 없습니다.")
        return

    print("\n[JSON 파일 목록]")
    for idx, file_path in enumerate(json_files, start=1):
        print(f"{idx}. {file_path}")

    try:
        idx = int(input("휴지통으로 보낼 파일 번호를 입력하세요: ")) - 1
        if 0 <= idx < len(json_files):
            move_to_trash(json_files[idx])
        else:
            print("잘못된 번호입니다.")
    except ValueError:
        print("유효한 번호를 입력하세요.")
