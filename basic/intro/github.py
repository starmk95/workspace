import requests

def get_github_user_info(username):
    """
    GitHub 사용자 정보를 가져오는 함수.
    
    매개변수:
        username (str): GitHub 사용자 계정명
    
    반환값:
        dict: 사용자 정보 (성공 시)
        str: 오류 메시지 (실패 시)
    """
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()  # 정상적으로 데이터를 가져오면 JSON 반환
    elif response.status_code == 404:
        return "❌ 존재하지 않는 GitHub 사용자입니다."
    else:
        return f"⚠️ 오류 발생 (HTTP 상태 코드: {response.status_code})"

# 사용자 입력 루프
while True:
    username = input("GitHub 계정을 입력하세요 (종료하려면 'exit' 입력): ").strip()

    if username.lower() == "exit":  # 'exit' 입력 시 종료
        print("프로그램을 종료합니다. 👋")
        break

    user_info = get_github_user_info(username)

    if isinstance(user_info, dict):  # 정상적으로 정보를 가져온 경우
        print("\n✅ 사용자 정보:")
        print(f"  - 이름: {user_info.get('name', '정보 없음')}")
        print(f"  - GitHub ID: {user_info.get('login', '정보 없음')}")
        print(f"  - 공개 저장소 수: {user_info.get('public_repos', '정보 없음')}")
        print(f"  - 팔로워 수: {user_info.get('followers', '정보 없음')}")
        print(f"  - 프로필 URL: {user_info.get('html_url', '정보 없음')}\n")
    else:
        print(user_info)  # 오류 메시지 출력


"""
def test_get_github_user_info():
    GitHub 사용자 정보 조회 함수의 정상 및 비정상 상태 테스트

    # ✅ 정상 계정 테스트 (존재하는 GitHub 계정)
    valid_user = "torvalds"  # 리눅스 창시자인 Linus Torvalds의 GitHub 계정
    valid_response = get_github_user_info(valid_user)
    assert isinstance(valid_response, dict), "✅ 정상 사용자 정보 가져오기 실패"
    print(f"✅ 테스트 성공: {valid_user} 정보 가져오기")

    # ❌ 비정상 계정 테스트 (존재하지 않는 계정)
    invalid_user = "thisuserdoesnotexist12345"
    invalid_response = get_github_user_info(invalid_user)
    assert invalid_response == "❌ 존재하지 않는 GitHub 사용자입니다.", "❌ 존재하지 않는 계정 테스트 실패"
    print(f"✅ 테스트 성공: {invalid_user} (존재하지 않음)")

    # ⚠️ 기타 HTTP 오류 테스트 (GitHub API 차단 또는 다운된 경우)
    error_user = ""  # 빈 문자열을 입력해 API가 예상치 못한 응답을 주는지 확인
    error_response = get_github_user_info(error_user)
    assert isinstance(error_response, str), "⚠️ API 오류 처리 실패"
    print(f"✅ 테스트 성공: 기타 오류 처리")

# 테스트 실행
test_get_github_user_info()
"""