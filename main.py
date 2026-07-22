# ==========================================
# Carbon AI Prompt Manager
# main.py
# ==========================================

from data import prompts
from prompt_manager import add_prompt


def show_menu():
    """메인 메뉴 출력"""
    print("\n" + "=" * 50)
    print("      Carbon AI Prompt Manager v1.0")
    print("=" * 50)
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("0. 종료")
    print("=" * 50)


def main():
    """프로그램 시작"""

    while True:

        show_menu()

        choice = input("메뉴를 선택하세요 : ")

        if choice == "1":
            add_prompt()

        elif choice == "2":
            print("\n[프롬프트 목록 기능은 다음 단계에서 구현합니다.]")

        elif choice == "3":
            print("\n[카테고리 조회 기능은 다음 단계에서 구현합니다.]")

        elif choice == "4":
            print("\n[검색 기능은 다음 단계에서 구현합니다.]")

        elif choice == "5":
            print("\n[상세 보기 기능은 다음 단계에서 구현합니다.]")

        elif choice == "6":
            print("\n[즐겨찾기 관리 기능은 다음 단계에서 구현합니다.]")

        elif choice == "7":
            print("\n[즐겨찾기 목록 기능은 다음 단계에서 구현합니다.]")

        elif choice == "0":
            print("\n프로그램을 종료합니다.")
            break

        else:
            print("\n잘못된 메뉴입니다. 다시 선택하세요.")


if __name__ == "__main__":
    main()