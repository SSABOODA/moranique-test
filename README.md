# Moranique Coding-Test
## API 구현 과제
1. 블로그 게시물 조회 (GET)
    - url: `api/blogs`
2. 블로그 게시물 작성 (POST)
    - url: `api/blog/create`

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
- http://18.220.46.183/api/blogs/
위의 url을 주소창에 입력하면 다음과 같이 DB에 저장된 블로그 게시물 목록을 조회할 수 있습니다.
```
[
    {
        "id": 1,
        "title": "테스트1",
        "created_at": "2021-09-08T07:32:51.245101Z",
        "user": "test1",
        "body": "테스트1",
        "user_id": 1
    },
    {
        "id": 2,
        "title": "테스트2",
        "created_at": "2021-09-08T07:34:29.442624Z",
        "user": "test1",
        "body": "테스트2",
        "user_id": 1
    },
    {
        "id": 3,
        "title": "테스트3",
        "created_at": "2021-09-08T08:23:58.291019Z",
        "user": "test1",
        "body": "테스트3",
        "user_id": 1
    },
    {
        "id": 4,
        "title": "테스트4",
        "created_at": "2021-09-08T08:29:33.874235Z",
        "user": "test1",
        "body": "테스트4",
        "user_id": 1
    },
    {
        "id": 5,
        "title": "test 0 테스트5",
        "created_at": "2021-09-08T08:48:01.687167Z",
        "user": "test0",
        "body": "test 0 테스트5",
        "user_id": 2
    },
    {
        "id": 6,
        "title": "test1 테스트 글6",
        "created_at": "2021-09-08T09:38:47.722968Z",
        "user": "test1",
        "body": "test1 테스트 글6",
        "user_id": 1
    },
    {
        "id": 7,
        "title": "test1 테스트 글7",
        "created_at": "2021-09-08T09:52:36.672533Z",
        "user": "test1",
        "body": "test1 테스트 글7",
        "user_id": 1
    },
    {
        "id": 8,
        "title": "test2 write",
        "created_at": "2021-09-08T14:11:57.891674Z",
        "user": "test2",
        "body": "test2 write",
        "user_id": 3
    }
]
```
- http://18.220.46.183/api/blog/create/
위의 url로 이동하면 blog 게시물을 등록할 수 있는 엔드포인트 화면이 나타납니다.