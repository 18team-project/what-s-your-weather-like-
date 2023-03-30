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
| 무드 등록 | /mood | {_id: ObjectId('6424b982c6e0eddaf1627558'),
user_nm: "치코리타",
comment: "오늘의 당신의 날씨는 어떤가요?,
"mood_icon: "😆",
date: "2023-03-29"} |중앙정렬|
|왼쪽정렬|오른쪽정렬|중앙정렬|중앙정렬|
|왼쪽정렬|오른쪽정렬|중앙정렬|중앙정렬|



