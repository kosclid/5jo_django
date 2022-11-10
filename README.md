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
pip install scipy

3. migrate
python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser
데이터베이스 슈퍼계정(관리자) 만들기

이후 데이터 베이스가 잘 연결되어 있다면 아래코드가 실행됩니다.
add_data_movie.py
add_data_ost.py
add_data_nomal.py
차례대로 실행 (데이터 베이스에 데이터 저장하는 과정)
