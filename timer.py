import time
import subprocess
import os
import sys
from datetime import datetime, timedelta

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SCRIPT_DIR = os.path.join(BASE_DIR, "tools", "productivity", "scripts")

def ensure_directory_exists(directory):
    """디렉토리가 존재하지 않으면 생성합니다."""
    if not os.path.exists(directory):
        os.makedirs(directory)

def create_completion_script(message):
    """완료 메시지를 표시하는 스크립트를 생성합니다."""
    ensure_directory_exists(SCRIPT_DIR)
    script_path = os.path.join(SCRIPT_DIR, "completion_script.py")
    with open(script_path, "w", encoding="utf-8") as file:
        file.write(f"""
print("{message}")
input("엔터를 눌러 창을 닫으세요...")
""")
    return script_path

def display_progress_bar(duration):
    """타이머 진행률을 표시하는 게이지 바를 출력합니다."""
    for elapsed in range(duration + 1):
        progress = int((elapsed / duration) * 50)  # 50칸으로 나눈 진행률
        bar = "█" * progress + "-" * (50 - progress)
        sys.stdout.write(f"\r[{bar}] {elapsed}/{duration}초")
        sys.stdout.flush()
        time.sleep(1)
    print()  # 진행률 완료 후 줄바꿈

def display_remaining_time(target_time):
    """남은 시간을 실시간으로 표시합니다."""
    while True:
        now = datetime.now()
        remaining_time = target_time - now
        if remaining_time.total_seconds() <= 0:
            break
        minutes, seconds = divmod(int(remaining_time.total_seconds()), 60)
        sys.stdout.write(f"\r남은 시간: {minutes}분 {seconds}초")
        sys.stdout.flush()
        time.sleep(1)
    print()  # 진행 완료 후 줄바꿈

def set_timer():
    """타이머를 설정하고 완료 시 새로운 터미널 창에서 알림을 표시합니다."""
    try:
        seconds = int(input("타이머 시간을 초 단위로 입력하세요: "))
        print(f"{seconds}초 타이머가 시작되었습니다.")
        display_progress_bar(seconds)  # 게이지 바 표시
        print("\n⏰ 타이머 종료! 알림이 울립니다.")
        script_path = create_completion_script("⏰ 타이머가 종료되었습니다!")
        subprocess.Popen(["python", script_path], creationflags=subprocess.CREATE_NEW_CONSOLE)
    except ValueError:
        print("유효한 숫자를 입력하세요.")

def set_alarm():
    """알람을 설정하고 완료 시 새로운 터미널 창에서 알림을 표시합니다."""
    try:
        alarm_time_str = input("알람 시간을 HH:MM 형식으로 입력하세요 (24시간제): ")
        alarm_time = datetime.strptime(alarm_time_str, "%H:%M").replace(
            year=datetime.now().year,
            month=datetime.now().month,
            day=datetime.now().day
        )
        if alarm_time < datetime.now():
            alarm_time += timedelta(days=1)  # 다음 날로 설정
        print(f"알람이 {alarm_time.strftime('%H:%M')}에 설정되었습니다.")
        display_remaining_time(alarm_time)  # 남은 시간 표시
        print("\n⏰ 알람 시간입니다! 알림이 울립니다.")
        script_path = create_completion_script("⏰ 알람 시간이 되었습니다!")
        subprocess.Popen(["python", script_path], creationflags=subprocess.CREATE_NEW_CONSOLE)
    except ValueError:
        print("유효한 HH:MM 형식의 시간을 입력하세요.")
    except Exception as e:
        print(f"알람 설정 중 오류가 발생했습니다: {e}")

def timer_menu():
    """타이머/알림 메뉴를 출력하고 사용자 입력을 처리합니다."""
    while True:
        print("\n[타이머/알림 메뉴]")
        print("[1] 타이머 설정")
        print("[2] 알람 설정")
        print("[b] 돌아가기")
        choice = input(">> 원하는 작업을 선택하세요: ")
        if choice == "1":
            set_timer()
        elif choice == "2":
            set_alarm()
        elif choice == "b":
            break
        else:
            print("잘못된 입력입니다. 다시 시도하세요.")
