# ==========================================
# Carbon AI Prompt Manager
# prompt_manager.py
# ==========================================

from data import prompts


# 기본 카테고리
CATEGORIES = [
    "탄소데이터",
    "ESG",
    "보고서",
    "자동화",
    "페르소나",
    "기타"
]


def add_prompt():
    """
    새로운 프롬프트를 추가하는 함수
    """

    print("\n" + "=" * 50)
    print("        프롬프트 추가")
    print("=" * 50)

    # -------------------------
    # 제목 입력
    # -------------------------
    while True:

        title = input("제목 : ").strip()

        if title != "":
            break

        print("제목은 비워둘 수 없습니다.")

    # -------------------------
    # 내용 입력
    # -------------------------
    while True:

        content = input("내용 : ").strip()

        if content != "":
            break

        print("내용은 비워둘 수 없습니다.")

    # -------------------------
    # 카테고리 선택
    # -------------------------
    print("\n카테고리 선택")

    for i, category in enumerate(CATEGORIES, start=1):
        print(f"{i}. {category}")

    print("0. 직접 입력")

    while True:

        choice = input("선택 : ").strip()

        # 숫자인지 확인
        if not choice.isdigit():
            print("숫자를 입력하세요.")
            continue

        choice = int(choice)

        # 직접 입력
        if choice == 0:

            while True:

                category = input("새 카테고리 입력 : ").strip()

                if category != "":
                    break

                print("카테고리는 비워둘 수 없습니다.")

            break

        # 기존 카테고리
        elif 1 <= choice <= len(CATEGORIES):

            category = CATEGORIES[choice - 1]
            break

        else:

            print("올바른 번호를 선택하세요.")

    # -------------------------
    # 프롬프트 저장
    # -------------------------
    prompt = {
        "title": title,
        "content": content,
        "category": category,
        "favorite": False
    }

    prompts.append(prompt)

    print("\n프롬프트가 성공적으로 추가되었습니다!")

    print(f"현재 등록된 프롬프트 수 : {len(prompts)}개")

def show_prompt_list():
    """
    저장된 모든 프롬프트 목록 출력
    """

    print("\n" + "=" * 50)
    print("              프롬프트 목록")
    print("=" * 50)

    # 프롬프트가 없는 경우
    if len(prompts) == 0:
        print("등록된 프롬프트가 없습니다.")
        return

    # 프롬프트 목록 출력
    for index, prompt in enumerate(prompts, start=1):

        # 즐겨찾기 여부
        star = "⭐" if prompt["favorite"] else ""

        print(
            f"{index}. "
            f"[{prompt['category']}] "
            f"{prompt['title']} {star}"
        )

    print("-" * 50)
    print(f"총 {len(prompts)}개의 프롬프트가 등록되어 있습니다.")

def filter_by_category():
    """
    카테고리별 프롬프트 조회
    """

    print("\n" + "=" * 50)
    print("          카테고리별 조회")
    print("=" * 50)

    # 카테고리 출력
    for index, category in enumerate(CATEGORIES, start=1):
        print(f"{index}. {category}")

    # 번호 입력
    while True:

        choice = input("\n카테고리를 선택하세요 : ").strip()

        if not choice.isdigit():
            print("숫자를 입력하세요.")
            continue

        choice = int(choice)

        if 1 <= choice <= len(CATEGORIES):
            break

        print("올바른 번호를 입력하세요.")

    selected_category = CATEGORIES[choice - 1]

    print("\n" + "=" * 50)
    print(f"[{selected_category}] 프롬프트 목록")
    print("=" * 50)

    count = 0

    for index, prompt in enumerate(prompts, start=1):

        if prompt["category"] == selected_category:

            star = "⭐" if prompt["favorite"] else ""

            print(f"{index}. {prompt['title']} {star}")

            count += 1

    print("-" * 50)

    if count == 0:
        print("해당 카테고리에 등록된 프롬프트가 없습니다.")
    else:
        print(f"총 {count}개의 프롬프트가 있습니다.")

def search_prompt():
    """
    키워드로 프롬프트 검색
    (제목 또는 내용에서 검색)
    """

    print("\n" + "=" * 50)
    print("              프롬프트 검색")
    print("=" * 50)

    keyword = input("검색어를 입력하세요 : ").strip()

    if keyword == "":
        print("검색어를 입력해야 합니다.")
        return

    print("\n" + "=" * 50)
    print("검색 결과")
    print("=" * 50)

    count = 0

    for index, prompt in enumerate(prompts, start=1):

        if (keyword.lower() in prompt["title"].lower() or
                keyword.lower() in prompt["content"].lower()):

            star = "⭐" if prompt["favorite"] else ""

            print(
                f"{index}. "
                f"[{prompt['category']}] "
                f"{prompt['title']} {star}"
            )

            count += 1

    print("-" * 50)

    if count == 0:
        print("검색 결과가 없습니다.")
    else:
        print(f"{count}개의 프롬프트를 찾았습니다.")

def show_prompt_detail():
    """
    프롬프트 상세 보기
    """

    print("\n" + "=" * 50)
    print("            프롬프트 상세 보기")
    print("=" * 50)

    # 프롬프트가 없는 경우
    if len(prompts) == 0:
        print("등록된 프롬프트가 없습니다.")
        return

    # 번호 입력
    while True:

        choice = input("프롬프트 번호를 입력하세요 : ").strip()

        if not choice.isdigit():
            print("숫자를 입력하세요.")
            continue

        choice = int(choice)

        if 1 <= choice <= len(prompts):
            break

        print("올바른 번호를 입력하세요.")

    prompt = prompts[choice - 1]

    star = "⭐" if prompt["favorite"] else ""

    print("\n" + "=" * 50)
    print("프롬프트 상세 정보")
    print("=" * 50)

    print(f"번호       : {choice}")
    print(f"제목       : {prompt['title']}")
    print(f"카테고리   : {prompt['category']}")
    print(f"즐겨찾기   : {star}")

    print("-" * 50)

    print("내용")
    print("-" * 50)
    print(prompt["content"])

    print("=" * 50)

