# What's your weather like?
## 프로젝트 개요

## 프로젝트 구조
```bash
├── static
│   ├── css
│   ├── img
│   ├── js
│   └── video
├── templates
│   └── common
│       ├── delete.html
│       ├── layout.html
│       ├── pop.html
│       └── popup.html
│   ├── home.html
│   ├── login.html
│   ├── mood.html
│   ├── mypage.html
│   └── register.html
└── app.py

```
## 구현 기능
-무드등록
  - method : get
  - url : 
  - 담당 : 신주영

-나의 무드 조회
  - method : post
  - url : /mood
  - 담당 : 신희제, 신주영, 박하은
 
-로그인
  - method : post
  - url : /login
  - 담당 : 박하은
 
-회원가입
  - method : post
  - url : /register
  - 담당 : 신주영
  
-무드 삭제
  - method : post
  - url : /delete
  - 담당 : 박하은


## API 설계
| Aa기능 | method | request | 담당 |
|:---|:---|:---|:---|
| 무드 등록 | /mood | [{_id: ObjectId('6424b982c6e0eddaf1627558'), user_nm: "항해", comment: "오늘의 당신의 날씨는 어떤가요?, "mood_icon: "😆", date: "2023-03-29"}, {_id: ObjectId('6424b982c6e0eddaf1627558'), user_nm: ”김말순",comment: "봄이다! 오늘이 가장 젊은날!, "mood_icon: "😆", date: "2023-03-29"}] |  |
| 나의 무드 조회 | /mypage | {user_nm:’최민호’, user_pw:’*****’} | {'msg': '당신의 날씨를 등록 했습니다.'} |
| 로그인 | /login | {user_nm:’최민호’, user_pw:’*****’} | {'msg': '당신의 날씨를 등록 했습니다.'} |
| 회원가입 | /register | {user_nm:’최민호’, user_pw:’*****’} | {'msg': '당신의 날씨를 등록 했습니다.'} |


* 세션 추가 오류
 * 로그인 기능을 도입하니 세션이 필요했다. 하지만? 그렇다 우리 조는 프론트 머리 밖에 없다. 돌아가지 않는 서버를 벅벅 긁으며   세션을 추가해보았지만 오류만 났다. 애초에 세션이 저장이 안됐다.
  왜 오류가 발생하였는가? html 파일에 <body>태그 밑에 <script>가 있어서 작동하지 않았다.
  오류 해결 시도 방법 : 세션에 대한 많은 함수를 시행해보고 임의로 세션을 지정해보기도 했지만 개발자 도구에 올라가지 않았다.
  오류 해결 방법 : 스크립트를 헤더에 넣으니 정상 작동 됐다.

