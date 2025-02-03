import re

def validate_password(password):
    """
    비밀번호가 최소 하나의 소문자, 대문자, 숫자, 기호를 포함하는지 검증하는 함수
    """
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).{8,}$'
    
    if re.match(pattern, password):
        return True
    else:
        return False

# 사용자 입력 받기
password = input("비밀번호를 입력하세요: ")

if validate_password(password):
    print("✅ 유효한 비밀번호입니다!")
else:
    print("❌ 유효하지 않은 비밀번호입니다. (대소문자, 숫자, 특수문자 포함 & 8자 이상)")
