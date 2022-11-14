1. 가상환경 설치
python -m venv venv
venv\Scripts\activate

2. 라이브러리 설치
python -m pip intall "django==4.1.0“
python -m pip install "django~=4.1"
python -m pip install --upgrade pip
python -m pip install wheel

pip install django-bootstrap5
pip install Mysqlclient
pip install Pillow
pip install scipy

3. migrate
마이그래이션 하기전에 accounts, recommand폴더에 migrations폴더 들어가서
데이터 베이스는 밀어야 합니다...모델 다시 수정 했어요..

__init__.py외에 다른 파일(0001_initial.py같은)있는지 확인하고 있으면 삭제하세요
__init__.py은 지우면 안되요!!!

이후 마이그래이션 진행하면 됩니다.
python manage.py makemigrations
python manage.py migrate

데이터베이스 슈퍼계정(관리자) 만들기
python manage.py createsuperuser

이후 데이터 베이스가 잘 연결되어 있다면 아래코드가 실행됩니다.
add_data_movie.py
add_data_ost.py
add_data_nomal.py
차례대로 실행 (데이터 베이스에 데이터 저장하는 과정)