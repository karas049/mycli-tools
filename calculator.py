import math

def basic_operations():
    """기본 산술 연산을 수행합니다."""
    try:
        expression = input("수식을 입력하세요 (예: 2 + 3 * 4): ")
        result = eval(expression)
        print(f"결과: {result}")
    except Exception as e:
        print(f"오류가 발생했습니다: {e}")

def advanced_operations():
    """고급 수학 연산을 수행합니다."""
    print("\n[고급 연산 목록]")
    print("[1] 제곱근 (sqrt)")
    print("[2] 거듭제곱 (pow)")
    print("[3] 로그 (log)")
    print("[4] 삼각 함수 (sin, cos, tan)")
    print("[b] 돌아가기")
    choice = input(">> 원하는 작업을 선택하세요: ")

    try:
        if choice == "1":
            num = float(input("숫자를 입력하세요: "))
            print(f"제곱근: {math.sqrt(num)}")
        elif choice == "2":
            base = float(input("밑수를 입력하세요: "))
            exp = float(input("지수를 입력하세요: "))
            print(f"거듭제곱: {math.pow(base, exp)}")
        elif choice == "3":
            num = float(input("숫자를 입력하세요: "))
            base = input("로그의 밑수를 입력하세요 (기본값: e): ")
            if base:
                print(f"로그: {math.log(num, float(base))}")
            else:
                print(f"로그: {math.log(num)}")
        elif choice == "4":
            angle = float(input("각도를 입력하세요 (도 단위): "))
            radians = math.radians(angle)
            print(f"sin({angle}) = {math.sin(radians)}")
            print(f"cos({angle}) = {math.cos(radians)}")
            print(f"tan({angle}) = {math.tan(radians)}")
        elif choice == "b":
            return
        else:
            print("잘못된 입력입니다.")
    except Exception as e:
        print(f"오류가 발생했습니다: {e}")

def calculator_menu():
    """계산기 메뉴를 출력하고 사용자 입력을 처리합니다."""
    while True:
        print("\n[계산기 메뉴]")
        print("[1] 기본 연산")
        print("[2] 고급 연산")
        print("[b] 돌아가기")
        choice = input(">> 원하는 작업을 선택하세요: ")
        if choice == "1":
            basic_operations()
        elif choice == "2":
            advanced_operations()
        elif choice == "b":
            break
        else:
            print("잘못된 입력입니다. 다시 시도하세요.")
