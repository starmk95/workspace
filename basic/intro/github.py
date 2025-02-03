import requests

def get_github_user_info(username):
    """
    GitHub 사용자 정보 및 저장소 목록을 가져오는 함수.
    
    매개변수:
        username (str): GitHub 사용자 계정명
    
    반환값:
        dict: 사용자 정보 (성공 시)
        str: 오류 메시지 (실패 시)
    """
    user_url = f"https://api.github.com/users/{username}"
    repos_url = f"https://api.github.com/users/{username}/repos"

    # 사용자 정보 요청
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        return "❌ 존재하지 않는 GitHub 사용자입니다." if user_response.status_code == 404 else f"⚠️ 오류 발생 (HTTP 상태 코드: {user_response.status_code})"

    user_data = user_response.json()

    # 저장소 정보 요청
    repos_response = requests.get(repos_url)
    repos_data = repos_response.json() if repos_response.status_code == 200 else []

    return {
        "user": user_data,
        "repos": repos_data
    }

# 사용자 입력 루프
while True:
    username = input("GitHub 계정을 입력하세요 (종료하려면 'exit' 입력): ").strip()

    if username.lower() == "exit":  # 'exit' 입력 시 종료
        print("프로그램을 종료합니다. 👋")
        break

    result = get_github_user_info(username)

    if isinstance(result, str):  # 오류 발생 시
        print(result)
    else:
        user_info = result["user"]
        repos = result["repos"]

        print("\n✅ 사용자 정보:")
        print(f"  - 이름: {user_info.get('name', '정보 없음')}")
        print(f"  - GitHub ID: {user_info.get('login', '정보 없음')}")
        print(f"  - 공개 저장소 수: {user_info.get('public_repos', '정보 없음')}")
        print(f"  - 팔로워 수: {user_info.get('followers', '정보 없음')}")
        print(f"  - 프로필 URL: {user_info.get('html_url', '정보 없음')}\n")

        print("📂 사용자 공개 저장소 목록:")
        if repos:
            for idx, repo in enumerate(repos[:10], start=1):  # 최대 10개 출력
                print(f"  {idx}. {repo['name']} | ⭐ {repo['stargazers_count']} | 🍴 {repo['forks_count']} | 🔗 {repo['html_url']}")
        else:
            print("  🚫 공개 저장소 없음")
        
        print("\n" + "=" * 50 + "\n")  # 구분선


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