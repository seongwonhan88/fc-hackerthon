# FC 9th Hackerthon

## Project Detail 
 - 해커톤 주제 : 세상을 변화시키는 소소한 움직임  
 - 프로젝트 목표 : 현재 진행중인 전시들을 보여주는 정적 페이지를 구성한다. 
 - 주제와의 일치 : 문화생활을 사람들에게 조금 더 가깝게 하는 소소한 움직임 구성 

## Members & Roles
- 김태철 : 데이터 크롤링(interpark 티켓링크에서 전시 관련 데이터 수집), 마스터 브랜치 운영(서비스 QA)
- 이정화 : 전시 관련 데이터베이스 구성 및 사용자 요청을 처리하는 비즈니스 로직 구현 
- 한성원 : 사용자 관련 데이터베이스 구성 및 정적페이지 view 처리

### Contraint  
 - 시간 관계상 서비스 배포는 진행하지 않음  


## installation  

### Requirements  
 - python 3.6   
 `pip install -r requirements.txt` 

### secrets 
 `.secrets/base.json`  
 
 - base.json
     ~~~
    {
        "SECRET_KEY" : "<SECRET_KEY>",
        "FACEBOOK_APP_ID" : "<FACEBOOK_APP_ID>",
        "FACEBOOK_APP_SECRET" : "<FACEBOOK_APP_SECRET>"
        "SOCIAL_AUTH_GOOGLE_OAUTH2_KEY":"<SOCIAL_AUTH_GOOGLE_OAUTH2_KEY>",
        "SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET":"<SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET>"
    }
    ~~~  
    
## Model  

### Show  
 - title, period, place, thumbnail, poster, description, price, created_at, web_link  
 - pick_users(MTM)

### Comment  
 - content, created_at
 - show(FK_Show), author(FK_User)
 
### ShowPick  
 - created_at 
 - show(FK_Show), user(FK_User)

### User  
 - AbstractUser  
 

## Tools and Third-Party Used
### Bootstrap 
### Django-Social-Auth  
### Jupyter Notebook, Selenium 


## Product Demo

### Site Demo  
<iframe width="560" height="315" src="https://www.youtube.com/embed/0Z6teoPhpfU" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>  


### Crawling Demo  

<iframe width="560" height="315" src="https://www.youtube.com/embed/IGP3VIPQIN4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>