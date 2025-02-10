def require_login(func):
    def wrapper(user):
        if user.get("is_logged_in"):
            return func(user)
        else:
            print("로그인이 필요합니다.")
    return wrapper

@require_login
def dashboard(user):
    print(f"{user['name']}님의 대시보드입니다.")

user1 = {"name": "Alice", "is_logged_in": True}
user2 = {"name": "Bob", "is_logged_in": False}
dashboard(user1) # 정상 실행
dashboard(user2) # 비정상 
