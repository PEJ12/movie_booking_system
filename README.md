# 🎬 Movie Booking System

## 📌 프로젝트 개요
이 프로젝트는 Flask를 활용한 **영화 예매 시스템**입니다. 사용자는 웹 애플리케이션을 통해 영화 정보를 조회하고, 예매 및 취소할 수 있습니다.

## 🚀 주요 기능
1. **영화 조회**
   - 상영 예정 영화 목록 출력
   - 영화 제목을 검색하여 상영 영화 확인
   - 상영 날짜 기준으로 영화 정렬
2. **영화 예매 및 취소**
   - 사용자가 원하는 영화를 선택하여 예매 가능
   - 예매된 영화는 취소할 수 있음
3. **사용자 역할**
   - 일반 사용자(User): 영화 예매 및 취소 가능
   - 직원(Staff): 멤버 정보 조회, 영화 정보 갱신, 평점 조회 및 추가
   - 분석가(Analyst): 영화 관람 정보 분

## 🛠 기술 스택
- **Backend**: Python (Flask), SQLite3
- **Frontend**: HTML, CSS
- **Server**: AWS EC2 (Ubuntu)

## 📂 프로젝트 구조
```
movie_booking_system/
│── app.py                # Flask 애플리케이션 실행 파일
│── models.py             # 데이터베이스 모델 정의
│── routes.py             # 라우트 핸들러
│── templates/            # HTML 템플릿 파일
│── movies.db             # SQLite 데이터베이스 파일
```


