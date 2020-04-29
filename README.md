﻿# StockAlarmBot
1. 프로젝트명 : 주가 알리미봇(StockAlarmBot)

2. 프로젝트 구성
    1) 카카오톡 채팅방에 카카오톡봇을 생성후 초대
    2) 채팅방에 있는 사람이 명령어 입력
        Ex) 주가 MSFT
    3) 봇이 답을 해줌.
        Ex) MSFT 165.60 +2.11 (1.29%)

3. 기획의도
    주가를 보려면 주식앱에 들어가서 확인해야 되는데 주식앱은 
    켤때 보안 프로그램 실행하기 때문에 시간이 걸림. 따라서 실시간으로 주가를 확인하기 귀찮음
    또한 미국장의 경우 주식앱에서는 15분의 딜레이를 가지고 주가를 보여주기 때문에
    항상 구글링을 통해서 확인을 해야 하는 상황.
    따라서 접근성이 있는 카카오톡을 이용하여 검색을 빠르게 도와주는 주가알리미봇이 필요함.

4. 개발해야 할 기능
    프론트엔드 : 웹앱이 아니기 때문에 따로 웹페이지 디자인 필요 X.
                 카카오톡 봇이 프론트엔드 역할
                 사용자로부터 받은 명령을 백엔드로 전달하는 기능 
    
    백엔드 : 카카오톡 봇(프론트엔드)와 연동하는 기능 개발 (SDK)
            주가를 알려주는 특정 웹사이트(investing.com)으로부터 크롤링하는 기능
            전달받은 명령어를 토대로 검색하는 기능

    DB : 크롤링해서 데이터를 전달해주기 때문에 따로 DB는 불필요. (But 기능추가시 DB 필요. Ex) 사용자마다 봇을 불러올수 있는 횟수 제한 등)

5. 개발 계획
    백엔드부터 : 크롤링 기능, 검색 기능 먼저 개발
    카카오톡 봇 만들기
    카카오톡 SDK 활용하기

6. 코드발표

6-1. 취지 & 설명 

주가를 실시간으로 확인해보고 싶을 때, 구글링을 통해 검색하거나 아니면 주식앱을 통해 확인을 해야하는데 
이는 너무 번거롭다. 더군다나 미국 주식의 경우 주식앱에서는 15분정도 딜레이되어 주가를 반영하기 때문에 실시간으로
주가를 확인하기 어려운 점이 있다. 따라서 이런 불편한 점을 개선하기 위해 접근성이 뛰어난 카카오톡 봇을 만들어
사용자가 원하는 주식을 입력했을 때 곧바로 카카오톡 봇이 대답을 해주는 프로그램을 만들었다.
더불어, 이를 오픈채팅방에서 활용한다면 여러 사람들이 주식을 검색하며 같은 종목을 보며 서로 의견을 나눌수 있는 여건이 만들어진다. 

6-2. 기술설명

프론트엔드
-카카오톡 봇 껍데기 
: 사람들에게 답변을 해줄 수 있도록 카카오톡 계정이 필요.
-메세지 인식 오픈소스 코드(.js) 
: 사람들이 메세지를 입력했을 때 그것을 파싱하여 올바른 명령어라면 요청을 백엔드로 전달하고 올바른 명령어가 아니라면 무시하는 역할. 
: 채팅 참여자의 메세지를 인식할 수 있는 모듈로 구글플레이스토어에 다운받아 사용할 수 있고, 메세지만 받아올수 있을뿐, 나머지는 자기가
직접 입맛에 맞게 js로 코딩해야함.


백엔드
-플라스크(.py)
: 프론트엔드에서 받은 request를 조건에 맞는 모듈로 라우팅해주고 받은 response를 다시 프론트엔드에 전달하는 역할.
-크롤링 모듈(.py) 
: 요청이 들어올때마다 주식 정보를 특정 사이트나 구글에서 크롤링하여 가져오는 역할.
: 크게 특정 종목의 주가, 지수, 선물 크롤링으로 나뉘어져 있음.   

6-3. 어려웠던 점 & 극복방법
<프론트엔드>
1. 카카오톡 가계정 생성
: 핸드폰 번호를 임의로 생성하고 해당 번호를 기반으로 카톡 가계정을 생성해야 되는데, 카톡측에서 악용방지를 위해
해당 계정에 친구 추가가 10명이상이 되어야 하고 일정 카톡을 주고받아야 하는 까다로운 정책을 걸어놔서
계정을 생성하고 활성화시키기 까지 꽤 오랜 기간이 걸림

2. 자바스크립트 작성
: 아직 자바스크립트 작성이 익숙하지 않아서 사용자 입력한 메세지가 명령어인지 아닌지 판단하기 위해 파싱하는 과정이
다소 까다로웠는데 구글링을 통해 자바스크립트에 익숙해지려고 노력함

<백엔드>
1. 플라스크 모듈 
: RESTFUL API 방식을 따라가려고 코딩규칙을 나름 세워서 진행했지만, 쉽지 않았음. RESTFUL API 까지는 아니더라도
HTTP API 방식까지는 구현한것 같음.

2. 크롤링 모듈
: 수업시간에 배웠던 파이썬에서의 http request 방법과 jsoup을 이용한 파싱을 통해 코드를 작성했으며 이부분은 그렇게 어렵지 않았음.
그러나 response을 주는 데이타의 타입을 json으로 할지, 딕셔너리로 할지, 리스트로 할지에 대해 많은 고민이 있었으며 
json으로 주는게 요즘 많이 쓰이는 방법이나 클라이언트에서 다시 파싱해야 되는 번거로움때문에 리스트로 주기로 결정.


6-4. 8주간의 코딩 첫걸음 후기
: 아무래도 파이썬이나 자바스크립트는 처음 접하다보니 어려움이 많았습니다. 그래도 8주동안 친절하신 튜터님을 잘 따라오면서 결국
저만의 서비스를 하나 만들었다는 점이 뿌듯합니다. 다음번에는 파이썬이 아니라 spring을 통해 웹서비스를 만들어보고 싶습니다.