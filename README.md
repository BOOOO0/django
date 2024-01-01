# Django

- `python -m venv [프로젝트명]`

- `./Scripts/activate.bat`

- manage.py - 엔트리 포인트? 프로젝트 내 장고 관련 명령 사용할때 사용

- settings.py - 환경 구성

- urls.py - URL 패턴, 경로

- `python manage.py runserver [포트 번호]` 기본 포트 번호는 8000

- Django는 프레임워크 내에 user, group이 존재

- 기본으로 제공되는 어드민 페이지에서 user, group 관리 가능하고 어드민 계정 생성 필요

- Django는 기본 sqlite3 DB 제공되고 프로젝트 생성 후 기본 테이블 생성 필요

- `python manage.py migrate`로 기본 테이블 생성

- `python manage.py createsuperuser`로 어드민 계정 생성

- 기본적으로 MVC 패턴을 가지고 있으며 models.py에서 모델을 정의한다.

- Django도 JPA처럼 코드로 데이터베이스 CRUD를 처리할 수 있다.

- Django Projenct 내에서 하나의 기능을 App이라고 한다. 단일 App으로도 가능하고 회원가입, 게시판 등을 각각의 App으로 생성해서 구현하면 복수의 App이 하나의 Project를 이루고 그것이 하나의 웹사이트이다.

- `python manage.py startapp [App명]`
