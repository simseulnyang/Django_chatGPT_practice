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

 <br>

 ## Channels
 - 장고 코어 프로젝트 : https://github.com/django/channels
 - ASGI 기반의 라이브러리, HTTP/웹소켓 프로토콜을 Django 친화적으로 지원
 - 2022년 10월에 v4.0.0 release
 - 필요한 라이브러리 : channels[daphne]~=4.0.0

 <br>

 ## TTS Engine (문자열을 음성으로 읽어주는 기능 - Text to Speech)
 - 운영체제/브라우저에서 음성합성 기능을 제공
 - 운영체제/브라우저마다 지원하는 언어 별 목소리 종류가 다름
 - Edge 브라우저에서의 목소리 지원이 Chrome등 다른 브라우저에 비해 다양한 편
 - 브라우저 기본에서 speechSynthesis 음성 합성 API를 제공함: 아직 실험적 API이기 때문에 모든 브라우저에서 지원되는 것은 아님(2024년 1월 현재, chrome 및 Edge 브라우저에서의 동작만 확인)
 - speechSynthesis.getVoices()호출하여 브라우저가 지원하는 목소리 목록을 얻을 수 있음

 ### assistant 응답을 ~~자동으로 읽어주기~~
 - 웹 브라우저 보안 정책으로 인해 사용자와의 상호작용(클릭 또는 탭)없이 speechSynthesis API를 통한 음성 합성을 시작하는 것은 허용되지 않음
 - 예) 페이지 로드와 함께 자동으로 음성 합성을 시작하려고 시도하면 "not-allowed"오류가 발생하게 됨

