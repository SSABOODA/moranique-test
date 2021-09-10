# Moranique Coding-Test
## API 구현 과제
1. 블로그 게시물 조회 (GET)
    - URL: `api/blogs`
2. 블로그 게시물 작성 (POST)
    - URL: `api/blog/create`

> Description

Ddjango REST framework를 사용하여 blog 게시물을 생성 및 조회하는 API를 구현하는 과제입니다.

> Environment
- Python 3.8
- Django REST Framework
- Conda
- Mysql
- Docker
- AWS(EC2, RDS)

> Project File Tree
```
├── accounts
|   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── blogs
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   ├── models.py
│   ├── permissions.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── moraniquetest
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── my_settings.py
├── requirements.txt
```

- requirement.txt : 프로젝트 실행을 위한 모든 설치파일(프레임워크, 라이브러리)들의 목록을 txt 형식으로 저장해놓은 파일입니다.
- my_settings.py : Github에 올라가면 안되는 프로젝트 설정 파일들이 있는 파일입니다. ex(DATABASE, SECETKEY_KEY)
- Dockerfile : Dcoker image를 생성하기 위한 파일입니다.
- accounts : User의 모델을 정의하고 회원가입, 로그인 관련 API를 구현하는 폴더입니다.
- blogs : User 정보를 활용하여 blog 게실물의 조회, 생성 API를 구현하는 폴더입니다.

> Usage

### 블로그 게시물 조회(GET)
- URL : http://18.220.46.183/api/blogs/

위의 url을 주소창에 입력하면 다음과 같이 DB에 저장된 블로그 게시물 목록을 조회할 수 있습니다.

![스크린샷 2021-09-10 오전 1 27 22](https://user-images.githubusercontent.com/69753846/132725261-b04fc1a4-fd87-4fa6-ba95-140461ff0cf0.png)


### 블로그 게시물 생성(POST)
- URL : http://18.220.46.183/api/blog/create/

위의 url로 이동하면 blog 게시물을 등록할 수 있는 엔드포인트 화면이 나타납니다.

![스크린샷 2021-09-10 오전 1 22 00](https://user-images.githubusercontent.com/69753846/132724716-63fd022c-738c-4a62-bbf6-06ce72e07b04.png)

- 인증 권한이 없는 비회원일 시 생성이 불가능하도록 구현하였습니다. 
- 우측 상단 Login 버튼을 눌러 로그인을 진행합니다.
- 아이디 비밀번호가 없을 시 회원가입을 진행합니다.

### 회원가입
- URL : http://18.220.46.183:8000/user/signup/
- 다음 URL 입력 시 회원가입 할 수 있는 화면이 나타납니다.

<img width="1146" alt="스크린샷 2021-09-10 오후 3 07 33" src="https://user-images.githubusercontent.com/69753846/132808526-0362dddc-90a4-4639-89ad-70df8157aa3a.png">

- 회원가입 이후에 우측 상단 Login 버튼을 눌러 회원가입한 정보로 login 진행 해주시고
- URL : http://18.220.46.183/api/blog/create/
- 다시 위의 URL로 이동합니다.

![스크린샷 2021-09-10 오전 1 25 50](https://user-images.githubusercontent.com/69753846/132725083-d5b3fecc-0b31-4d9f-bffa-f26f1b78543f.png)

- input 창에 제목과 내용을 작성하고 post하면 게시물이 생성됩니다.

![스크린샷 2021-09-10 오전 1 26 54](https://user-images.githubusercontent.com/69753846/132725162-fa4f7207-1f40-4aca-9a6c-a25b05434d4e.png)

