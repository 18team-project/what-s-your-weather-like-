# What's your weather like?
## 프로젝트 개요
```
항해 14기, 토이프로젝트
감정을 날씨에 비유, 본인의 감정을 기록하고 추적할 수 있는 형태의 게시판 구현
실시간 현재 날씨 정보를 가져와서 배경으로 나타낸다.
```
## 기술스택

<img src="https://simpleicons.org/icons/python.svg" style="width:120px; height: 120px; margin:3px;"></img>
<img src="https://simpleicons.org/icons/flask.svg" style="width:120px; height: 120px; margin:3px;"></img>
<img src="https://simpleicons.org/icons/mongodb.svg" style="width:120px; height: 120px; margin:3px;"></img>
<img src="https://simpleicons.org/icons/html5.svg" style="width:120px; height: 120px; margin:3px;"></img>
<img src="https://simpleicons.org/icons/css3.svg" style="width:120px; height: 120px; margin:3px;"></img>
<img src="https://simpleicons.org/icons/javascript.svg" style="width:120px; height: 120px; margin:3px;"></img>

<br>
<br>
<strong>#pythonㅤㅤ#flaskㅤㅤ#mongodbㅤㅤ#html5ㅤㅤ#css3ㅤㅤ#javascript</strong>



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
  - 담당 : 신희제, 신주영

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

-실시간 날씨 정보
  - method : 
  - url : 
  - 담당 : 신주영

## API 설계
| Aa기능 | method | request | 담당 |
|:---|:---|:---|:---|
| 무드 등록 | /mood | [{_id: ObjectId('6424b982c6e0eddaf1627558'), user_nm: "항해", comment: "오늘의 당신의 날씨는 어떤가요?, "mood_icon: "😆", date: "2023-03-29"}, {_id: ObjectId('6424b982c6e0eddaf1627558'), user_nm: ”김말순",comment: "봄이다! 오늘이 가장 젊은날!, "mood_icon: "😆", date: "2023-03-29"}] |  |
| 나의 무드 조회 | /mypage | {user_nm:’최민호’, user_pw:’*****’} | {'msg': '당신의 날씨를 등록 했습니다.'} |
| 로그인 | /login | {user_nm:’최민호’, user_pw:’*****’} | {'msg': '당신의 날씨를 등록 했습니다.'} |
| 회원가입 | /register | {user_nm:’최민호’, user_pw:’*****’} | {'msg': '당신의 날씨를 등록 했습니다.'} |

## 트러블 슈팅


1. 세션 추가 오류 : 로그인 기능을 도입하니 세션이 필요했다. 하지만? 그렇다 우리 조는 프론트 머리 밖에 없다. 돌아가지 않는 서버를 벅벅 긁으며 세션을 추가해보았지만 오류만 났다. 
애초에 세션이 저장이 안됐다.
왜 오류가 발생하였는가? html 파일에 <body>태그 밑에 <script>가 있어서 작동하지 않았다.
오류 해결 시도 방법 : 세션에 대한 많은 함수를 시행해보고 임의로 세션을 지정해보기도 했지만 개발자 도구에 올라가지 않았다.
오류 해결 방법 : 스크립트를 헤더에 넣으니 정상 작동 됐다.

2. 파이선 세션 추가 오류 : 로그인 기능을 도입하니 세션이 필요했다. 하지만? 그렇다 우리 조는 프론트 머리 밖에 없다. 돌아가지 않는 서버를 벅벅 긁으며 세션을 추가해보았지만 오류만 났다. 애초에 세션이 저장이 안됐다.
왜 오류가 발생하였는가? html 파일에 <body>태그 밑에 <script>가 있어서 작동하지 않았다.
오류 해결 시도 방법 : 세션에 대한 많은 함수를 시행해보고 임의로 세션을 지정해보기도 했지만 개발자 도구에 올라가지 않았다.
오류 해결 방법 : 스크립트를 헤더에 넣으니 정상 작동 됐다.

3. 날씨 API 추가 오류 : 발급받은 API키를 사용하는 와중에 자꾸 인가되지 않은 키라고 요청이 무시되었다
오류 해결 시도 : 구글링을 하다보니 해당 api를 제공하는 서비스가 유료로 전환이 되었다고 하였습니다. 공공 api를 받아오는 방법으로 시도하려 했지만 개발 기간이 촉박해서 다른 방법을 생각해야 했습니다.
오류 해결 방법 : 날씨 정보 사이트의 접속 위치를 기반으로 현재 날씨를  검색해 웹사이트 크롤링을 하는 방법으로 해결 했습니다.
