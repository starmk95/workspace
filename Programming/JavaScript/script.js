document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault(); // 폼 제출 시 페이지 새로 고침 방지
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    // 입력값 검증 (예: 이메일 형식 체크)

    if (!email || !password) {
    alert("모든 필드를 채워 주세요.");
    return;
    }
    // 메시지 표시
    const message = `로그인 성공!<br>이메일: ${email}`;
    document.getElementById('message').innerHTML = message;
    });

