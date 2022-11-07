1. 가상환경 설치
PS C:\workspace\esg-a-django> python -m venv venv
PS C:\workspace\esg-a-django> venv\Scripts\activate

2. 라이브러리 설치
(venv) PS C:\workspace\esg-a-django> python -m pip intall "django==4.1.0“s
(venv) PS C:\workspace\esg-a-django> python -m pip install "django~=4.1" 
4.1버전중 최신버전 설치

(venv) PS C:\workspace\esg-a-django> python -m pip install --upgrade pip
(venv) PS C:\workspace\esg-a-django> python -m pip install wheel

pip install django-bootstrap5
pip install Mysqlclient
pip install Pillow

3. migrate
(venv) PS C:\workspace\esg-a-django> python .\manage.py showmigrations
migrate해야하는 목록 보여줌

(venv) PS C:\workspace\esg-a-django> python manage.py makemigrations
blog에 migrations 파일을 만들어줌
(venv) PS C:\workspace\esg-a-django> python manage.py migrate
장고 코드에 맞도록 데이터베이스 만들어줌

(venv) PS C:\workspace\esg-a-django> python manage.py createsuperuser
데이터베이스 슈퍼계정(관리자) 만들기

장고 설치 제외하고는 새로운 프로젝트 때마다 해줘야함