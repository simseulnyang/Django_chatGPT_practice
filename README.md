# Django_chatGPT_practice

## 필요한 기술
### 1. 동적 웹페이지 생성을 도와주는 프레임 워크
 - Python
 - Django

### 2. 실시간 서버/클라이언트 통신을 위한 웹소켓(WebSocket)
 - 클라이언트 : 최신 웹브라우저 기본에서 지원
 - 서버 : Django Channels

### 3. 상황극 상대자
 - OpenAI API를 통한 응답 자동 생성

<br>

## OpenAI API 활용
### 1. 텍스트 생성 또는 문서 요약
 - 2023년 6월 기준 "text-davinci-003" engine 사용
 - 예시 ) 간단한 문법 오류 수정

### 2. 챗봇 응답 생성
 - 2023년 6월 기준 "gpt-3.5-turbo" model 사용
 - messages 인자로 대화내역 리스트를 지정하며, 각 message에는 "role", "content" 라는 2가지의 key를 사용한다.
 - "role"은 "system", "user", "assistant"만을 지정할 수 있고, "content"에는 대화 내용 문자열을 담는다.