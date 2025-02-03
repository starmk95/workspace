import re

def validate_password(password):
    """
    비밀번호가 최소 하나의 소문자, 대문자, 숫자, 기호를 포함하는지 검증하는 함수
    """
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).{8,}$'
    
    return bool(re.match(pattern, password))  # True 또는 False 반환

# 사용자 입력 루프
while True:
    password = input("비밀번호를 입력하세요 (종료하려면 'exit' 입력): ")

    if password.lower() == "exit":  # 'exit' 입력 시 종료
        print("프로그램을 종료합니다. 👋")
        break

    if validate_password(password):
        print("✅ 유효한 비밀번호입니다!")
    else:
        print("❌ 유효하지 않은 비밀번호입니다. (대소문자, 숫자, 특수문자 포함 & 8자 이상)")
