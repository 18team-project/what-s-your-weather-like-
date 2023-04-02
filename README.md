# What's your weather like?
## 프로젝트 개요
```
항해 14기, 토이프로젝트

감정을 날씨에 비유, 본인의 감정을 기록하고 추적할 수 있는 감정트래커 프로젝트.
실시간 현재 날씨 정보를 가져와서 배경으로 나타낸다.

사용자 ux/ui 고려 (슬라이더, div 팝업 모달, 사용자 이용 흐름 고려)
```
## 기술스택
```
#pythonㅤㅤ#flaskㅤㅤ#mongodbㅤㅤ#html5ㅤㅤ#css3ㅤㅤ#javascript
```
<p align="center">
<img src="https://simpleicons.org/icons/python.svg" style="width:120px; height: 120px; margin:3px;"></img>
<img src="https://simpleicons.org/icons/flask.svg" style="width:120px; height: 120px; margin:3px;"></img>
<img src="https://simpleicons.org/icons/mongodb.svg" style="width:120px; height: 120px; margin:3px;"></img>
<img src="https://simpleicons.org/icons/html5.svg" style="width:120px; height: 120px; margin:3px;"></img>
<img src="https://simpleicons.org/icons/css3.svg" style="width:120px; height: 120px; margin:3px;"></img>
<img src="https://simpleicons.org/icons/javascript.svg" style="width:120px; height: 120px; margin:3px;"></img>
</p>

## 프로젝트 구조
```bash
├── 📂 static
│   ├── 📁 css
│   ├── 📁 img
│   ├── 📁 js
│   └── 📁 video
├── 📂 templates
│   ├── 📂 common
│   │   ├── 📄delete.html
│   │   ├── 📄layout.html
│   │   ├── 📄pop.html
│   │   └── 📄popup.html
│   ├── 📄home.html
│   ├── 📄login.html
│   ├── 📄mood.html
│   ├── 📄mypage.html
│   └── 📄register.html
└── 🏃app.py

```
## 구현 내용
- 무드등록
  - method : get
  - url : 
  - 담당 : 신희제, 신주영

- 나의 무드 조회
  - method : post
  - url : /mood
  - 담당 : 신희제, 신주영, 박하은
 
- 로그인
  - method : post
  - url : /login
  - 담당 : 박하은
 
- 회원가입
  - method : post
  - url : /register
  - 담당 : 신주영
  
- 무드 삭제
  - method : post
  - url : /delete
  - 담당 : 신희제, 박하은

- 실시간 날씨 정보
  - method : 
  - url : 
  - 담당 : 신주영

## API 설계
| <center>API 기능</center> | **method** | **요청** | **응답** |
|---|---|---|---|
| 무드 등록 | /mood | {user_nm:String, user_pw:String} | {msg: String} |
| 나의 무드 조회 | /mypage | {user_nm:String} | [{_id:Object, user_nm:String, comment:String,</br>mood_icon: String, date: String},</br>{_id:Object, user_nm: String, comment:String,</br>mood_icon:String, date:String}]|
| 로그인 | /login | {user_nm:String, user_pw:String} | {msg: String} |
| 회원가입 | /register | {user_nm:String, user_pw:String} | {msg: String} |

## 트러블 슈팅


1. <b>세션 추가 오류</b></br>`상황` 로그인 기능을 도입하니 세션이 필요했다. 하지만? 그렇다 우리 조는 프론트 머리 밖에 없다. 돌아가지 않는 서버를 벅벅 긁으며 세션을 추가해보았지만 오류만 났다. 
애초에 세션이 저장이 안됐다.</br>
`원인`  html 파일에 `<body>`태그 밑에 `<script>`가 있어서 작동하지 않았다.</br>
`시도`  세션에 대한 많은 함수를 시행해보고 임의로 세션을 지정해보기도 했지만 개발자 도구에 올라가지 않았다.</br>
`해결`  스크립트를 헤더에 넣으니 정상 작동 됐다.

2. <b>서버 세션 생성 오류</b></br>`상황` 로그인 기능을 위해 세션을 생성해야 하는데 python, flask 개발환경에서 세션값을 생성하지 못함. </br>
`원인` 파이선 환경 설정 및 라이브러리 사용에 익숙치 않아 트러블 슈팅이 어려웠다.</br>
`시도` 쿠키에 로그인 정보를 적용하는 방법도 생각해 보았지만 로그인 유지를 위한 값이기 때문에 사용자 로컬에 저장되는 쿠키는 적합하지 않다고 생각하였다.</br>
`해결` 자바스크립크에서 웹 스토리지를 사용(세션스토리지 및 로컬스토리지)

3. <b>날씨 API 추가 오류</b></br>`상황` 발급받은 API키를 사용하는 와중에 자꾸 인가되지 않은 키라고 요청이 무시되었다</br>
`원인` 해당 api 유료 전환</br>
`시도` 공공 api를 받아오는 방법으로 시도하려 했지만 개발 기간이 촉박해서 다른 방법을 생각해야 했습니다.</br>
`해결` 날씨 정보 사이트의 접속 위치를 기반으로 현재 날씨를 검색해 웹사이트 크롤링을 하는 방법으로 해결 했습니다.

## 구현 화면
<p align="center">
<img  style="height:262px; margin:10px;" src="https://user-images.githubusercontent.com/58963027/228920210-5efafdb8-d303-4d4c-a333-dade7dcacd0e.gif"></img>
<img style="width:480px; hight:277px; margin:10px;" src="https://user-images.githubusercontent.com/58963027/228920999-85209f79-ea54-42a4-b413-c144c984055d.gif"></img>
</p>


